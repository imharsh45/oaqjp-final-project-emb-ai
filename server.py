from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_api():
    """Handles the GET request for emotion detection."""
    text_to_analyze = request.args.get("textToAnalyze")

     # Validate input
    if not text_to_analyze:
        return "Error : No Text provided. Please enter a valid statement."

    # If dominant emotion is None, return an error message
    if response["dominant_emotion"] is None:
         return "Invalid text! Please try again."
           

     # Call the emotion detection function
    response = emotion_detector(text_to_analyze)

    # Format the response
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_response

@app.route("/")
def render_index_page():
    """Renders the main web interface page."""
    return render_template('index.html')

# Run the application on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)