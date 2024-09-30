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