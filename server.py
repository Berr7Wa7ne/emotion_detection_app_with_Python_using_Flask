"""
Module to run a Flask application for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to detect emotions in the provided text.

    Returns:
        str: Response message indicating the detected emotion or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)

    if dominant_emotion is None or dominant_emotion.get('dominant_emotion') is None:
        return "Invalid text! Please try again."

    detected_emotion = dominant_emotion['dominant_emotion']
    return f"The given text has been identified as {detected_emotion}."

@app.route("/")
def render_index_page():
    """
    Endpoint to render the index.html template.

    Returns:
        str: Rendered HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
