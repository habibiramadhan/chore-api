from fastapi import APIRouter, status, HTTPException
from app.transaction.schemas import CreateTransactionModel
from app.transaction.service import TransactionService
from app.database import db_dependency

transaction_router = APIRouter()
transaction_service = TransactionService()

# POST
@transaction_router.post("/")
async def create_transaction(transaction:CreateTransactionModel, db : db_dependency):
    try:
        new_transaction = await transaction_service.create_transaction(transaction, db)
        return {"status": "OK", "data": new_transaction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# GET
@transaction_router.get("/")
async def get_all_transactions(db:db_dependency):
    try:
        result = await transaction_service.get_all_transactions(db)
        return {"status": "OK", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@transaction_router.get("/{transaction_id}")
async def get_transaction_by_id(transaction_id:int, db:db_dependency):
    try:
        result = await transaction_service.get_transaction_by_id(transaction_id, db)
        if result:
            return {"status": "OK",  "data":result}
        else:
            raise HTTPException(status_code=404, detail=f"Transaction-{transaction_id} is not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))