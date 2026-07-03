from fastapi import FastAPI

app = FastAPI(
    title="TechDocAI",
    descryption= "Multimodal RAG System for Technical Documents",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project":"TechDocAI",
        "message": "Backend running Successfully......",
        "version": "1.0.0"
    }