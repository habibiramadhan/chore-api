import app.models as models
from app.transaction.schemas import CreateTransactionModel
from app.models import Transaction
from app.database import db_dependency

class TransactionService:
    async def create_transaction(self, transaction: CreateTransactionModel, db : db_dependency):
        transaction_data_dict = transaction.model_dump()
        new_transaction = Transaction(**transaction_data_dict)
        db.add(new_transaction)
        db.commit()
        db.refresh(new_transaction)
        return new_transaction
    
    # Delete
    async def delete_transaction(self, transaction_id:int, db:db_dependency):
        transaction = db.query(models.Transaction).filter(models.Transaction.transaction_id == transaction_id).first()
        if transaction:
            db.delete(transaction)
            db.commit()
            return transaction
        return