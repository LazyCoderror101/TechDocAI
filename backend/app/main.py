import shutil
from fastapi import FastAPI, UploadFile, File

app = FastAPI(
    title="TechDocAI",
    description="Multimodal RAG System for Technical Documents",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project":"TechDocAI",
        "message": "Backend running Successfully......",
        "version": "1.0.0"
    }

@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):
    file_path = f"storage/{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "path": file_path,
        "message": "PDF Saved successfully"
    }