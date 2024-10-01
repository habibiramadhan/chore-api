from pydantic import BaseModel
from typing import Optional
import app.models as models
from datetime import date

class CreateTransactionModel(BaseModel):
    date: Optional[date]
    name: str
    category: models.TransactionCategory
    description: Optional[str]
    nominal: float

class UpdateTransactionModel(BaseModel):
    date: Optional[date]
    name: Optional[str]
    category: Optional[models.TransactionCategory]
    description: Optional[str]
    nominal: Optional[float]