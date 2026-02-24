from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load emotion model (this may take some time first run)
emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=False
)

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Emotion AI Backend is running 🚀"}

@app.post("/detect-emotion")
def detect_emotion(request: TextRequest):
    result = emotion_pipeline(request.text)
    
    emotion = result[0]["label"]
    confidence = result[0]["score"]
    
    return {
        "emotion": emotion,
        "confidence": round(confidence, 4)
    }