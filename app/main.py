from fastapi import FastAPI
from app.database import db_dependency, engine
from app.models import User, Base
from app.auth.routes import router as auth_router  

app = FastAPI()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
