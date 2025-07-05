# EduRecommend - AI Course Recommendation System

A beautiful and intelligent course recommendation system that helps users discover personalized learning paths using AI-powered content analysis.

## ✨ Features

- **AI-Powered Recommendations**: Uses TF-IDF vectorization and cosine similarity to find relevant courses
- **Beautiful UI**: Modern, professional design with smooth animations
- **Real-time Search**: Instant course recommendations based on user input
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Smart Filtering**: Intelligent preprocessing of course descriptions and skills

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install required packages**
   ```bash
   pip install flask pandas scikit-learn spacy
   ```

3. **Download spaCy language model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. **Prepare your data**
   - Make sure you have a `courses.csv` file in the project root
   - The CSV should contain columns: `title`, `description`, `skills_covered`, `duration`, `level`, `platform`, `url`

### Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

3. **Start discovering courses!**
   - Enter skills or course topics you want to learn
   - Get AI-powered recommendations instantly

## 📁 Project Structure

```
course-recommendation-system/
├── app.py              # Main Flask application
├── model.py            # AI recommendation engine
├── courses.csv         # Course dataset
├── templates/
│   └── index.html      # Beautiful frontend interface
└── README.md           # This file
```

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **AI/ML**: scikit-learn, spaCy for natural language processing
- **Data**: Pandas for data manipulation
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Styling**: Custom CSS with gradients and animations

## 📊 How It Works

1. **Data Processing**: Course descriptions are preprocessed using spaCy (tokenization, lemmatization, stop word removal)
2. **Vectorization**: Text is converted to numerical vectors using TF-IDF
3. **Similarity Calculation**: User input is compared with course vectors using cosine similarity
4. **Ranking**: Top 5 most similar courses are returned and displayed

## 💡 Usage Examples

Try searching for:
- "machine learning"
- "web development" 
- "data science"
- "digital marketing"
- "python programming"

## 🎯 Features in Detail

- **Smart Search**: Understands synonyms and related concepts
- **Professional UI**: Clean, modern design with smooth animations
- **Loading States**: Beautiful loading indicators during search
- **Error Handling**: User-friendly error messages
- **Responsive**: Works on all screen sizes
- **Performance**: Fast recommendations using optimized algorithms

## 📝 Data Format

Your `courses.csv` should have these columns:
- `title`: Course name
- `description`: Detailed course description
- `skills_covered`: Skills and topics covered
- `duration`: Course duration
- `level`: Difficulty level (Beginner/Intermediate/Advanced)
- `platform`: Learning platform name
- `url`: Course URL

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Learning! 🎓**
