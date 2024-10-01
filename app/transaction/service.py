import app.models as models
from app.transaction.schemas import CreateTransactionModel, UpdateTransactionModel
from app.models import Transaction
from app.database import db_dependency

class TransactionService:
    # Create
    async def create_transaction(self, transaction: CreateTransactionModel, username: str, db : db_dependency):
        transaction_data_dict = transaction.__dict__
        new_transaction = Transaction(**transaction_data_dict)
        new_transaction.username = username
        db.add(new_transaction)
        db.commit()
        db.refresh(new_transaction)
        return new_transaction
    
    # Delete
    async def delete_transaction(self, transaction_id:int, username: str, db:db_dependency):
        transaction = db.query(Transaction).filter(
                Transaction.transaction_id == transaction_id,
                (Transaction.username == username) if username!="admin" else True
            ).first()
        if transaction:
            db.delete(transaction)
            db.commit()
            return transaction
        return
      
    # update
    async def update_transaction(self, transaction_id:int, username: str, transaction_update: UpdateTransactionModel, db:db_dependency):
        transaction = db.query(Transaction).filter(
                Transaction.transaction_id == transaction_id,
                (Transaction.username == username) if username!="admin" else True
            ).first()
        if transaction:
            transaction.date = transaction_update.date if transaction_update.date else transaction.date
            transaction.name = transaction_update.name if transaction_update.name else transaction.name
            transaction.category = transaction_update.category if transaction_update.category else transaction.category
            transaction.description = transaction_update.description if transaction_update.description else transaction.description
            transaction.nominal = transaction_update.nominal if transaction_update.nominal else transaction.nominal
            
            db.commit()
            db.refresh(transaction)
            return transaction
        return
    # Get
    async def get_all_transactions(self, username: str,db : db_dependency):
        transactions = db.query(Transaction).filter((Transaction.username == username) if username!="admin" else True).all()
        return transactions
    
    async def get_transaction_by_id(self, transaction_id: int, username: str, db: db_dependency):
        transaction = db.query(Transaction).filter(
                Transaction.transaction_id == transaction_id,
                (Transaction.username == username) if username!="admin" else True
            ).first()
        return transaction
    
    async def get_transactions_filtered(self, transaction_category:str, transaction_name:str, username: str, db:db_dependency):
        transactions = db.query(Transaction).filter(
                (Transaction.category == transaction_category) if transaction_category else True,
                (Transaction.name.like(f"%{transaction_name}%")) if transaction_name else True,
                (Transaction.username == username) if username!="admin" else True
            ).all()
        return transactions
