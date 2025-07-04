from flask import Flask, render_template, request, jsonify
import pandas as pd
from model import get_model_data

app = Flask(__name__)

# Load data and functions from model.py
df, get_recommendations, transformed_corpus = get_model_data()

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for course recommendations (AJAX call)
@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['query']
    recommended_courses = get_recommendations(user_input, transformed_corpus)
    return jsonify(recommended_courses.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
