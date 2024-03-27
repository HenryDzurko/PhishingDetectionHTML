from flask import Flask, render_template, request
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the trained model
nb_classifier, tfidf_vectorizer = joblib.load('phishing_detection_model.pkl')

@app.route('/')
def index():
    return render_template('phishing_detection.html')

if __name__ == '__main__':
    app.run(debug=True)