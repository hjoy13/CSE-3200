from flask import Flask, render_template, request, jsonify
import pandas as pd
from model import get_model_data
import traceback

app = Flask(__name__)

# Load data and functions from model.py
try:
    df, get_recommendations, transformed_corpus = get_model_data()
    print(f"Model loaded successfully. Dataset shape: {df.shape}")
except Exception as e:
    print(f"Error loading model: {e}")
    df, get_recommendations, transformed_corpus = None, None, None

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for course recommendations (AJAX call)
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Check if model is loaded
        if df is None or get_recommendations is None:
            return jsonify({'error': 'Model not loaded properly'}), 500
        
        # Get user input
        user_input = request.form.get('query', '').strip()
        print(f"Received query: '{user_input}'")
        
        if not user_input:
            return jsonify({'error': 'No query provided'}), 400
        
        # Get recommendations
        recommended_courses = get_recommendations(user_input, transformed_corpus)
        print(f"Generated {len(recommended_courses)} recommendations")
        
        # Convert to dictionary format
        result = recommended_courses.to_dict(orient="records")
        
        # Debug: Print first recommendation
        if result:
            print(f"First recommendation: {result[0]}")
        
        return jsonify(result)
    
    except Exception as e:
        print(f"Error in recommend route: {e}")
        print(traceback.format_exc())
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(debug=True)