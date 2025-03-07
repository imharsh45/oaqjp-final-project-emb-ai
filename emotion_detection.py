import requests  # Import requests to send HTTP requests
import json  # Import JSON library for response formatting

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion expressed in the given text using Watson NLP API.

    :param text_to_analyze: The input text to analyze.
    :return: A dictionary containing emotion scores and the dominant emotion.
    """
    # Watson NLP API URL for Emotion Detection
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # API request headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Constructing the request payload
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Sending a POST request to the Watson NLP API
    response = requests.post(url, json=myobj, headers=headers)

    # Convert the response to a dictionary
    formatted_response = json.loads(response.text)

    print("Raw API Response:", formatted_response)  # Debugging step

    # Extract emotion scores from the correct API response structure
    emotions = formatted_response.get("emotionPredictions", [])
    
    if not emotions:
        return {"error": "No emotion data found in API response"}

    # Extract the "emotion" dictionary
    emotion_scores = emotions[0].get("emotion", {})

    # Ensure all required emotions are included (default to 0 if missing)
    required_emotions = ["anger", "disgust", "fear", "joy", "sadness"]
    emotion_scores = {emotion: emotion_scores.get(emotion, 0.0) for emotion in required_emotions}

    # Find the dominant emotion (highest score)
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Add the dominant emotion to the output
    emotion_scores["dominant_emotion"] = dominant_emotion

    return emotion_scores
