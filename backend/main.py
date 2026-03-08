from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from formatter import format_message

# Create FastAPI app
app = FastAPI(title="Emotion Detection API")

# Load emotion model (returns all emotion scores)
classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)
# Request schema
class TextRequest(BaseModel):
    text: str


# Root endpoint
@app.get("/")
def home():
    return {"message": "Emotion Detection API is running 🚀"}
@app.post("/detect-emotion")
def detect_emotion(request: TextRequest):
    try:
        text = request.text.strip()

        results = classifier(text)[0]

        sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)

        dominant = sorted_results[0]

        formatted = format_message(text, dominant["label"])

        return {
            "original_text": text,
            "emotion": dominant["label"],
            "confidence": round(dominant["score"] * 100, 2),
            "formatted_message": formatted
        }

    except Exception as e:
        return {"error": str(e)}