import requests
import os
class API:
    def __init__(self):
        self.api = os.environ.get('HF_API') #'Hugging Face API'
        self.headers = {"Authorization": f"Bearer {self.api}"}
    def ner(self, text):
        API_URL = "https://api-inference.huggingface.co/models/dbmdz/bert-large-cased-finetuned-conll03-english"
        payload = {"inputs": text}
        response = requests.post(API_URL, headers=self.headers, json=payload)
        return response.json()
    def sentiment_analysis(self, text):
        API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
        payload = {"inputs": text}
        response = requests.post(API_URL, headers=self.headers, json=payload)
        return response.json()
    def emotion(self, text):
        API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
        payload = {'inputs': text}
        response = requests.post(API_URL, headers=self.headers, json=payload)
        return response.json()

