from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message" : "Emotion AI Backend is running"}

@app.get("/health")
def health_check():
    return{"status" : "Healthy"}