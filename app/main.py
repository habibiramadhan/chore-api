from fastapi import FastAPI
from app.database import db_dependency
import app.models as models
from app.database import engine, SessionLocal

app=FastAPI()

# create the table
models.Base.metadata.create_all(bind=engine)