"""
This module initiates the Flask application for the Emotion Detection
service. It provides routes for rendering the index page and
processing emotion detection requests.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyzes the text provided in the request and returns emotion scores.
    If the input is invalid, returns an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    label = response['dominant_emotion']
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    # Check if the dominant_emotion is None (for error handling)
    if label is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the sentiment analysis results
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {label}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application page (index.html) over the Flask app.
    """
    # This function renders the main application page
    return render_template('index.html')

if __name__ == "__main__":
    # Start the Flask application on port 5000
    app.run(host="0.0.0.0", port=5000)
