import requests
import json
def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj={ "raw_document": { "text": text_to_analyze } }
    response=requests.post(url,json=obj,headers=headers)
    dictionary=json.loads(response.text)
    if response.status_code==200:
        emotion=dictionary["emotionPredictions"][0]["emotion"]
        emotion["dominant_emotion"]=max(emotion,key=emotion.get)
        return emotion
    elif response.status_code==400:
        return{
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
            }
    