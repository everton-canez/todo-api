from fastapi import FastAPI
from models import Base
from routers import auth, todos
from database import engine  # Add this import if engine is defined in database.py

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)

