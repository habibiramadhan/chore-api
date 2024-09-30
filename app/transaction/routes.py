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
    
# DELETE
@transaction_router.delete("/{transaction_id}")
async def delete_transaction(transaction_id:int, db:db_dependency):
    try:
        deleted_transaction = await transaction_service.delete_transaction(transaction_id, db)
        if deleted_transaction:
            return deleted_transaction
        raise HTTPException(status_code=404, detail=f"Transaction-{transaction_id} doesn't exist")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))