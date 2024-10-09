from fastapi import APIRouter, status, HTTPException, Depends, UploadFile
from app.rag.service import RAGService
from app.database import db_dependency
from app.auth.routes import get_current_user
import fitz

rag_router = APIRouter()
rag_service = RAGService()

# POST
@rag_router.post("/")
async def add_rag_document(file:UploadFile, db:db_dependency, current_user: str = Depends(get_current_user)):
    try:
        await rag_service.add_documents(current_user, file, db)
        return {"status":"OK", "data":"Document added successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))