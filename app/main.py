from fastapi import FastAPI
from app.database import db_dependency, engine
from app.models import User, Base
from app.auth.routes import router as auth_router  
import app.models as models
from app.transaction.routes import transaction_router


app = FastAPI()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Include the authentication routes
app.include_router(auth_router, prefix="/auth", tags=["auth"])

# Include the transaction routes
app.include_router(transaction_router, prefix="/transaction", tags=["transaction"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
