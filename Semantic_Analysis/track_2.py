import pandas as pd
import numpy as np
import re
import string
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from sklearn.model_selection import train_test_split
from sklearn.pipeline import FeatureUnion
import gensim.downloader as api
from sentence_transformers import SentenceTransformer

def load_data():
    dev_responses = pd.read_csv('dev_responses.csv')
    train_responses = pd.read_csv('train_responses.csv')
    return pd.concat([dev_responses, train_responses], ignore_index=True)

def preprocess_text(text):
    text = text.lower().strip()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

combined_data = load_data()
test_prompts=pd.read_csv('test_prompts.csv')

combined_data['user_prompt'] = combined_data['user_prompt'].astype(str)
combined_data['model_response'] = combined_data['model_response'].astype(str)

combined_data['processed_prompt'] = combined_data['user_prompt'].apply(preprocess_text)
test_prompts['processed_prompt'] = test_prompts['user_prompt'].apply(preprocess_text)

text_model = api.load("word2vec-google-news-300")

def get_embedding(prompt, model):
    words = prompt.split()
    valid_vectors = [model[tok] for tok in words if tok in model.key_to_index]
    return np.mean(valid_vectors, axis=0) if valid_vectors else np.zeros(model.vector_size)

train_embeddings = np.vstack([get_embedding(prompt, text_model) for prompt in combined_data['processed_prompt']])
test_embeddings = np.vstack([get_embedding(prompt, text_model) for prompt in test_prompts['processed_prompt']])

similarities = cosine_similarity(test_embeddings, train_embeddings)

top_indices = np.argmax(similarities, axis=1)
retrieved_responses = combined_data.iloc[top_indices]['conversation_id'].values

answers=pd.DataFrame({})
answers['conversation_id']=test_prompts['conversation_id']
answers['response_id']=retrieved_responses

answers.reset_index(drop=True, inplace=True)
answers.to_csv('track_2_test.csv')