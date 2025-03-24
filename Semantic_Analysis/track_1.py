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

ngram_range_w = (1,2)
ngram_range_c = (2,4)
max_df = 0.80
min_df = 1

word_vectorizer = TfidfVectorizer(ngram_range=ngram_range_w, max_df=max_df, min_df=min_df, analyzer='word', sublinear_tf=True)
char_vectorizer = TfidfVectorizer(ngram_range=ngram_range_c, max_df=max_df, min_df=min_df, analyzer='char', sublinear_tf=True)
vectorizer = FeatureUnion([("word_tfidf", word_vectorizer), ("char_tfidf", char_vectorizer)])

tfidf_train = vectorizer.fit_transform(combined_data['processed_prompt'])
tfidf_test = vectorizer.transform(test_prompts['processed_prompt'])

similarities = cosine_similarity(tfidf_test, tfidf_train)
top_indices = np.argmax(similarities, axis=1)

retrieved_responses = combined_data.iloc[top_indices]['conversation_id'].values

answers=pd.DataFrame({})
answers['conversation_id']=test_prompts['conversation_id']
answers['response_id']=retrieved_responses

answers.reset_index(drop=True, inplace=True)
answers.to_csv('track_1_test.csv')