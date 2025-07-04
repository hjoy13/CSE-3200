import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

# Load dataset
df = pd.read_csv('courses.csv')
df.dropna(subset=['skills_covered'], inplace=True)

# Load Spacy model for NLP
nlp = spacy.load('en_core_web_sm')

def preprocess(skills_covered):
    """Function to process the course descriptions (skills covered)"""
    doc = nlp(skills_covered)
    filtered_token = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_token.append(token.lemma_)
    return " ".join(filtered_token)

# Apply preprocessing to the skills_covered column
df['preprocessed_skills'] = df['skills_covered'].apply(preprocess)

# Vectorization with TF-IDF
v = TfidfVectorizer()
transformed_corpus = v.fit_transform(df['preprocessed_skills'])

def get_recommendations(user_input, transformed_corpus):
    """Function to return top 5 recommended courses based on user input"""
    user_input_processed = preprocess(user_input)
    user_input_vector = v.transform([user_input_processed])
    cosine_similarities = cosine_similarity(user_input_vector, transformed_corpus).flatten()
    top_indices = cosine_similarities.argsort()[-5:][::-1]
    return df.iloc[top_indices]

# The following function will return the processed data and recommendation function
def get_model_data():
    return df, get_recommendations, transformed_corpus
