import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import numpy as np

# Load dataset
df = pd.read_csv('courses.csv')
df.dropna(subset=['skills_covered'], inplace=True)

# Load Spacy model for NLP
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    # Fallback if spacy model is not installed
    print("Warning: spacy model 'en_core_web_sm' not found. Install it with: python -m spacy download en_core_web_sm")
    nlp = None

def preprocess(skills_covered):
    """Function to process the course descriptions (skills covered)"""
    if nlp is None:
        # Simple fallback preprocessing if spacy is not available
        import re
        # Remove punctuation and convert to lowercase
        text = re.sub(r'[^\w\s]', ' ', str(skills_covered).lower())
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text
    
    doc = nlp(str(skills_covered))
    filtered_token = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_token.append(token.lemma_)
    return " ".join(filtered_token)

# Apply preprocessing to the skills_covered column
df['preprocessed_skills'] = df['skills_covered'].apply(preprocess)

# Vectorization with TF-IDF
v = TfidfVectorizer(max_features=5000, stop_words='english')
transformed_corpus = v.fit_transform(df['preprocessed_skills'])

def get_recommendations(user_input, transformed_corpus):
    """Function to return top 5 recommended courses based on user input"""
    user_input_processed = preprocess(user_input)
    user_input_vector = v.transform([user_input_processed])
    cosine_similarities = cosine_similarity(user_input_vector, transformed_corpus).flatten()
    
    # Get top 5 indices
    top_indices = cosine_similarities.argsort()[-5:][::-1]
    
    # Get the recommended courses
    recommended_courses = df.iloc[top_indices].copy()
    
    # Add similarity scores
    recommended_courses['similarity_score'] = cosine_similarities[top_indices]
    
    # Clean up NaN values before returning
    recommended_courses = recommended_courses.fillna({
        'title': 'No Title Available',
        'description': 'No description available',
        'duration': 'Duration not available',
        'level': 'Level not specified',
        'url': '',
        'course_certificate_type': 'Not mentioned',
        'enrolled_students': 'Not mentioned',
        'rating': 'Not mentioned'
    })
    
    # Convert any remaining NaN to string
    for col in recommended_courses.columns:
        recommended_courses[col] = recommended_courses[col].astype(str)
        recommended_courses[col] = recommended_courses[col].replace('nan', 'Not available')
        recommended_courses[col] = recommended_courses[col].replace('NaN', 'Not available')
    
    return recommended_courses

# The following function will return the processed data and recommendation function
def get_model_data():
    return df, get_recommendations, transformed_corpus