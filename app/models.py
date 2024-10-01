from sqlalchemy import Column, ForeignKey, Integer, Float, String, Date, Enum, CheckConstraint, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
import enum
from datetime import date

class TransactionCategory(enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    transactions = relationship('Transaction', backref="users")

class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, ForeignKey('users.username'))
    date = Column(Date, default=date.today)
    name = Column(String, nullable=False)
    category = Column(Enum(TransactionCategory), index=True, nullable=False)
    description = Column(String)
    nominal = Column(Float, nullable=False)

    __table_args__ = (
        CheckConstraint('nominal > 0', name='check_nominal_gt_zero'),
    )
