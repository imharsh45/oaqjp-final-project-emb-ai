import requests  # Import requests to send HTTP requests

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion expressed in the given text using Watson NLP API.

    :param text_to_analyze: The input text to analyze.
    :return: The response text from Watson NLP Emotion Predict API.
    """
    # Watson NLP API URL for Emotion Detection
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # API request headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Constructing the request payload
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Sending a POST request to the Watson NLP API
    response = requests.post(url, json=myobj, headers=headers)

    # Returning the response text received from the API
    return response.text
