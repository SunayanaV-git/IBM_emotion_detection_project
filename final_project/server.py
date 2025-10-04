''' 
Server module for emotion detection
'''
from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route('/')
def template():
    '''
    Render the html template
    '''
    return render_template("index.html")

@app.route('/emotionDetector')
def emotion():
    '''
    Function calling to analyze emotion
    '''
    text_to_analyze=request.args.get('textToAnalyze')
    response=emotion_detector(text_to_analyze)

    anger=response["anger"]
    disgust=response["disgust"]
    fear=response["fear"]
    joy=response["joy"]
    sadness=response["sadness"]
    dominant_emotion=response["dominant_emotion"]

    if dominant_emotion is not None:
        return (f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}.")
    return "Invalid text!Please try again!"
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
    