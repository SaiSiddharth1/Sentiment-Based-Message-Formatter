from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

app = FastAPI()

emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

class TextRequest(BaseModel):
    text: str
@app.post("/detect-emotion")
def detect_emotion(request: TextRequest):
    cleaned_text = request.text.strip()

    sentences = sent_tokenize(cleaned_text)

    sentence_emotions = []

    for sentence in sentences:
        results = emotion_pipeline(sentence)[0]
        sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)
        top_emotion = sorted_results[0]

        sentence_emotions.append({
            "sentence": sentence,
            "emotion": top_emotion["label"],
            "confidence": round(top_emotion["score"], 4)
        })

    return {
        "total_sentences": len(sentence_emotions),
        "analysis": sentence_emotions
    }