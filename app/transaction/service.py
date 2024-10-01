import app.models as models
from app.transaction.schemas import CreateTransactionModel
from app.models import Transaction
from app.database import db_dependency

class TransactionService:
    # Create
    async def create_transaction(self, transaction: CreateTransactionModel, db : db_dependency):
        transaction_data_dict = transaction.model_dump()
        new_transaction = Transaction(**transaction_data_dict)
        db.add(new_transaction)
        db.commit()
        db.refresh(new_transaction)
        return new_transaction
    
    # Get
    async def get_all_transactions(self, db : db_dependency):
        transactions = db.query(Transaction).all()
        return transactions
    
    async def get_transaction_by_id(self, transaction_id: int, db: db_dependency):
        transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
        return transaction
    
    async def get_transactions_filtered(self, transaction_category:str, transaction_name:str, db:db_dependency):
        transactions = db.query(models.Transaction).filter(
                (Transaction.category == transaction_category) if transaction_category else True,
                (Transaction.name.like(f"%{transaction_name}%")) if transaction_name else True
            ).all()
        return transactions