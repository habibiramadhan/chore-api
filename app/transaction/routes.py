from fastapi import APIRouter, status, HTTPException, Depends
from app.transaction.schemas import CreateTransactionModel, UpdateTransactionModel
from app.transaction.service import TransactionService
from app.database import db_dependency
from app.auth.routes import get_current_user

transaction_router = APIRouter()
transaction_service = TransactionService()

# POST
@transaction_router.post("/")
async def create_transaction(transaction:CreateTransactionModel, db : db_dependency, current_user: str = Depends(get_current_user)):
    try:
        new_transaction = await transaction_service.create_transaction(transaction, db)
        return {"status": "OK", "data": new_transaction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# DELETE
@transaction_router.delete("/{transaction_id}")
async def delete_transaction(transaction_id:int, db:db_dependency, current_user: str = Depends(get_current_user)):
    try:
        deleted_transaction = await transaction_service.delete_transaction(transaction_id, db)
        if deleted_transaction:
            return deleted_transaction
        raise HTTPException(status_code=404, detail=f"Transaction-{transaction_id} doesn't exist")
    except Exception as e:
        if (str(e)==""):
            raise HTTPException(status_code=404, detail=f"Transaction-{transaction_id} doesn't exist")
        raise HTTPException(status_code=500, detail=str(e))

# PUT
@transaction_router.put("/{transaction_id}")
async def update_transaction(transaction_id:int, transaction_update:UpdateTransactionModel, db: db_dependency, current_user: str = Depends(get_current_user)):
    try:
        updated_transaction = await transaction_service.update_transaction(transaction_id, transaction_update, db) 
        if updated_transaction:
            return {"status": "OK", "data": updated_transaction}
        raise HTTPException(status_code=404, detail=f"Transaction-{transaction_id} doesn't exist")
    except Exception as e:
        if (str(e)==""):
            raise HTTPException(status_code=404, detail=f"Transaction-{transaction_id} doesn't exist")
        raise HTTPException(status_code=500, detail=str(e))
        
# GET
@transaction_router.get("/")
async def get_all_transactions(db:db_dependency, current_user: str = Depends(get_current_user)):
    try:
        result = await transaction_service.get_all_transactions(db)
        return {"status": "OK", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@transaction_router.get("/filtered")
async def get_transactions_filtered(*, transaction_category:str=None, transaction_name:str=None, db:db_dependency, current_user: str = Depends(get_current_user)):
    try:
        print("category:",transaction_category)
        print("name:",transaction_name)
        result = await transaction_service.get_transactions_filtered(transaction_category, transaction_name, db)
        if result:
            return {"status": "OK",  "data":result}
        raise HTTPException(status_code=404, detail=f"Transaction is not found")
    except Exception as e:
        if (str(e)==""):
            raise HTTPException(status_code=404, detail=f"Transaction is not found")
        raise HTTPException(status_code=500, detail=str(e))    
    
@transaction_router.get("/{transaction_id}")
async def get_transaction_by_id(transaction_id:int, db:db_dependency, current_user: str = Depends(get_current_user)):
    try:
        result = await transaction_service.get_transaction_by_id(transaction_id, db)
        if result:
            return {"status": "OK",  "data":result}
        raise HTTPException(status_code=404, detail=f"Transaction-{transaction_id} is not found")
    except Exception as e:
        if (str(e)==""):
            raise HTTPException(status_code=404, detail=f"Transaction-{transaction_id} is not found")
        raise HTTPException(status_code=500, detail=str(e))
