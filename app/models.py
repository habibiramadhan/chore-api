from sqlalchemy import Column, Integer, Float, String, Date, Enum, CheckConstraint
from app.database import Base
import enum
from datetime import date

class TransactionCategory(enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"

class User(Base):
    __tablename__= "user"
    
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Transaction(Base):
    __tablename__ = 'transaction'

    transaction_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(Date, default=date.today)
    name = Column(String, nullable=False)
    category = Column(Enum(TransactionCategory), index=True, nullable=False)
    description = Column(String)
    nominal = Column(Float, nullable=False)

    __table_args__ = (
        CheckConstraint('nominal > 0', name='check_nominal_gt_zero'),
    )