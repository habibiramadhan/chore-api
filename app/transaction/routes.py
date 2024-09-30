from fastapi import APIRouter, status, HTTPException
from app.transaction.schemas import CreateTransactionModel
from app.transaction.service import TransactionService
from app.database import db_dependency

transaction_router = APIRouter()
transaction_service = TransactionService()

@transaction_router.post("/")
async def create_transaction(transaction:CreateTransactionModel, db : db_dependency):
    try:
        new_transaction = await transaction_service.create_transaction(transaction, db)
        return {"status": "OK", "data": new_transaction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
