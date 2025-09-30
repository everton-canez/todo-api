from fastapi import FastAPI
from models import Base
from routers import admin, auth, todos, users
from database import engine  # Add this import if engine is defined in database.py

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

