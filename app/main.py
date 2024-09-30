from fastapi import FastAPI
import app.models as models
from app.database import engine
from app.transaction.routes import transaction_router
import uvicorn
import os

app=FastAPI()

# create the table
models.Base.metadata.create_all(bind=engine)

app.include_router(transaction_router, prefix="/transaction", tags=["transaction"])