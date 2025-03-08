AI-Based Emotion Detection Web App 🎭




📌 Project Overview
The AI-Based Emotion Detection Web App is a Flask-based web application that analyzes textual feedback and determines the dominant emotion using IBM Watson NLP. The application detects emotions such as anger, disgust, fear, joy, and sadness and provides a formatted response for user insights.

✅ Live Text Analysis - Input any text to analyze emotions
✅ IBM Watson NLP Integration - Advanced emotion detection
✅ Flask API Deployment - RESTful web service
✅ Error Handling & Unit Testing - Ensuring stability
✅ Static Code Analysis - Achieved a 10/10 PyLint score

🎯 Features
🔹 Emotion Detection - Detects joy, sadness, fear, anger, disgust
🔹 Real-time Web Interface - Simple UI for users to input text
🔹 REST API Support - Send text as an API request
🔹 Error Handling - Handles invalid inputs gracefully
🔹 Unit Testing & Static Code Analysis - Ensures robust performance
🔹 Deployment Ready - Hosted on Flask (localhost:5000)

🚀 Tech Stack
Python 3.11 - Backend logic
Flask - Web application framework
IBM Watson NLP API - Emotion analysis
HTML, JavaScript - Frontend UI
PyLint & Unit Tests - Code quality assurance


📂 Folder Structure
csharp
Copy
Edit
📦 AI-Based-Emotion-Detection
│-- EmotionDetection/             # Emotion Detection Module
│   │-- __init__.py               # Package Initialization
│   │-- emotion_detection.py      # Main NLP function
│
│-- static/                       # Static files (JS, CSS)
│   │-- mywebscript.js
│
│-- templates/                    # HTML templates
│   │-- index.html                 # UI for user input
│
│-- server.py                      # Flask Web Server
│-- test_emotion_detection.py      # Unit Test Cases
│-- README.md                      # Project Documentation
│-- LICENSE                        # Project License
🛠 Installation & Setup

1️⃣ Clone the repository

bash
Copy
Edit
git clone https://github.com/imharsh45/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai

2️⃣ Create a virtual environment (Optional, but recommended)

bash
Copy
Edit
python3.11 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
3️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Flask app

bash
Copy
Edit
python3.11 server.py
🌍 Open http://localhost:5000 in your browser.

📡 API Endpoints
Endpoint	Method	Description
/	GET	Loads the index.html web interface
/emotionDetector	GET	Analyzes text and returns emotions
📝 Example API Call
bash
Copy
Edit
curl "http://localhost:5000/emotionDetector?textToAnalyze=I%20love%20this%20new%20technology"
📤 Example API Response
json
Copy
Edit
{
    "anger": 0.006,
    "disgust": 0.002,
    "fear": 0.009,
    "joy": 0.968,
    "sadness": 0.049,
    "dominant_emotion": "joy"
}


🧪 Running Unit Tests
Run unit tests to validate the emotion detection functionality:

bash
Copy
Edit
python3.11 test_emotion_detection.py
✅ Expected Output

markdown
Copy
Edit
.....
----------------------------------------------------------------------
Ran 5 tests in 2.345s

OK
🛡 Static Code Analysis
To ensure code quality, we used PyLint:

bash
Copy
Edit
pylint server.py
✅ Achieved 10/10 score 🎯

📜 License
This project is open-source and available under the MIT License.


🌟 Contributing
Feel free to fork the repository and submit a pull request for improvements! 🚀

📢 If you like this project, give it a ⭐ on GitHub! 🎉
🔥 Happy Coding! 🚀
