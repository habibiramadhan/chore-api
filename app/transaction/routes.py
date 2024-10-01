from fastapi import APIRouter, status, HTTPException
from app.transaction.schemas import CreateTransactionModel, UpdateTransactionModel
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

# PUT
@transaction_router.put("/{transaction_id}")
async def update_transaction(transaction_id:int, transaction_update:UpdateTransactionModel, db: db_dependency):
    try:
        updated_transaction = await transaction_service.update_transaction(transaction_id, transaction_update, db) 
        if updated_transaction:
            return {"status": "OK", "data": updated_transaction}
        raise HTTPException(status_code=404, detail=f"Transaction-{transaction_id} doesn't exist")
        
# GET
@transaction_router.get("/")
async def get_all_transactions(db:db_dependency):
    try:
        result = await transaction_service.get_all_transactions(db)
        return {"status": "OK", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@transaction_router.get("/filtered")
async def get_transactions_filtered(*, transaction_category:str=None, transaction_name:str=None, db:db_dependency):
    try:
        print("category:",transaction_category)
        print("name:",transaction_name)
        result = await transaction_service.get_transactions_filtered(transaction_category, transaction_name, db)
        if result:
            return {"status": "OK",  "data":result}
        raise HTTPException(status_code=404, detail=f"Transaction is not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
    
@transaction_router.get("/{transaction_id}")
async def get_transaction_by_id(transaction_id:int, db:db_dependency):
    try:
        result = await transaction_service.get_transaction_by_id(transaction_id, db)
        if result:
            return {"status": "OK",  "data":result}
        raise HTTPException(status_code=404, detail=f"Transaction-{transaction_id} is not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
