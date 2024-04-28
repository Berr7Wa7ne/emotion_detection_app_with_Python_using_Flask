import json
import requests

def emotion_detector(text_to_analyze):
    """
    Run emotion detection using the appropriate Emotion Detection function.

    Args:
        text_to_analyze (str): The text to analyze.

    Returns:
        dict: A dictionary containing the emotion predictions.
    """
    # Check if the text to analyze is not empty
    if not text_to_analyze:
        print("Error: Text to analyze is empty!")
        return None
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        result = response.json()
        # Extract the emotion predictions
        emotion_predictions = result.get('emotionPredictions', [])
        # Check if there are any emotion predictions
        if emotion_predictions:
            return emotion_predictions[0]['emotion']
        else:
            print("Error: No emotion predictions found in the response!")
            return None
    elif response.status_code == 400:
        # If status_code is 400, return a dictionary with all values set to None
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:
        # If the request was not successful, print an error message and return None
        print(f"Error: Failed to analyze emotion. Status code: {response.status_code}")
        return None

        
def emotion_predictor(text_to_analyze):
    # Run emotion detection
    response_text = emotion_detector(text_to_analyze)
    response_dict = json.loads(response_text)

    # Extract emotion predictions
    emotion_predictions = response_dict['emotionPredictions'][0]['emotion']

    # Extract required emotions and their scores
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    emotion_scores = {emotion: emotion_predictions.get(emotion, 0.0) for emotion in emotions}

    # Find the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Format output
    output = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return output
