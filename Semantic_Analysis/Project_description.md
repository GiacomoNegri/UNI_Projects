# Title: Measuring Semantic Similarity
## Author: Giacomo Negri
## Date: 24/03/2025

# Introduction

This document describes a retrieval-based approach to measuring semantic similarity between user questions and responses in a conversational dataset. The goal is to find the most relevant response to a given test question by identifying the most similar question from a training dataset.

# Semantic Similarity in Conversational Retrieval

The task involves comparing a new question from the TEST set against a set of previously seen questions in the TRAIN+DEV datasets. The most similar question's response is returned as the predicted answer.

To achieve this, different text representation techniques are used:

- **Discrete Representations (Track 1)**: Representing text using TF-IDF, Count Vectorizer, or n-grams.
- **Distributed Representations (Track 2)**: Using pre-trained embeddings such as Word2Vec, FastText, or Doc2Vec.
- **Open Representations (Track 3)**: Combining multiple methods or using advanced embedding models.

# Text Representation Techniques

## **Track 1: Discrete Text Representation**

This approach represents text as a sparse matrix using discrete methods such as:

- **TF-IDF (Term Frequency-Inverse Document Frequency)**: This transforms text into a weighted numerical representation based on term importance.
  
  *TF-IDF Formula*:
  $$\text{TF-IDF}(w) = \text{TF}(w) \times \text{IDF}(w)$$
  
  Where:
  - $\text{TF}(w)$ is the term frequency of word $w$ in the document
  - $\text{IDF}(w) = \log\left(\frac{N}{\text{DF}(w)}\right)$, where $N$ is the total number of documents and $\text{DF}(w)$ is the document frequency of $w$

- **n-gram models**: Represents text as sequences of $n$ consecutive words or characters.
- **Count Vectorizer**: Converts text into frequency-based numerical representations.

Similarity between two questions is computed using **cosine similarity**:

$$\text{cosine}(A, B) = \frac{A \cdot B}{||A|| \, ||B||}$$

Where $A$ and $B$ are the TF-IDF or Count Vectorizer vectors of two questions.

## **Track 2: Distributed Static Text Representation**

This track utilizes **word embeddings**, which map words into dense vector spaces where similar words have closer representations. We use:

- **Word2Vec**: A neural-based model that learns word associations based on context using techniques like Skip-gram and CBOW.
- **FastText**: An extension of Word2Vec that considers subword information, allowing for better generalization.
- **Doc2Vec**: Extends Word2Vec to learn document-level representations.

For a given question $q$, the representation $v(q)$ is obtained by averaging the word embeddings of its words:

$$v(q) = \frac{1}{|W|} \sum_{w \in W} v(w)$$

Where:
- $W$ is the set of words in $q$
- $v(w)$ is the embedding of word $w$

Similarity is measured using **cosine similarity** or **Euclidean distance**:

$$d(A, B) = ||v(A) - v(B)||_2$$

## **Track 3: Open Text Representation (Bonus)**

In this optional track, a combination of discrete and distributed representations can be used, or more advanced models such as **BERT (Bidirectional Encoder Representations from Transformers)** can be implemented.

- **BERT-based sentence embeddings**: Uses transformer models like Sentence-BERT (SBERT) to obtain contextualized representations.
- **Hybrid methods**: Combining TF-IDF weighting with embeddings to improve performance.

# Evaluation

Performance is assessed using the **BLEU score**, which measures the overlap between the predicted and actual responses. BLEU evaluates precision on 1-4 gram overlaps:

*BLEU Score Formula*:
$$\text{BLEU} = \text{BP} \times \exp\left(\sum_{n=1}^{4} w_n \log P_n\right)$$

Where:
- $P_n$ is the precision for n-grams
- $w_n$ are weights (typically uniform)
- **BP** is the brevity penalty to handle short outputs

The final submission consists of CSV files containing conversation IDs and the retrieved response IDs.

# Execution

To run the retrieval model and generate predictions, follow these steps:

1. Install dependencies (`scikit-learn`, `gensim`, `nltk`, `pandas`, `numpy`).
2. Load and preprocess the dataset.
3. Compute text representations for TRAIN+DEV prompts.
4. Compare TEST prompts to TRAIN+DEV prompts using similarity metrics.
5. Retrieve the best-matching response.
6. Evaluate results using the BLEU score.
7. Generate CSV output files.

# Conclusion

This approach allows for efficient retrieval of relevant responses using semantic similarity. Discrete and distributed text representations provide strong baselines, while more advanced techniques can further enhance retrieval accuracy.
