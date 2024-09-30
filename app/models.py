from sqlalchemy import Column, Integer, Float, String, Date, Enum, CheckConstraint,Boolean
from app.database import Base
import enum
from datetime import date

class TransactionCategory(enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

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