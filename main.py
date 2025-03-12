from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

from models import Base, ProductDB
from database import engine, get_db
from auth import login, register, get_current_user, User, UserCreate
from pydantic import BaseModel

# ----------------- INIT APP ----------------- #
Base.metadata.create_all(bind=engine)
app = FastAPI()

# ----------------- SCHEMA ----------------- #


class Product(BaseModel):
    name: str
    price: float
    description: str
    image_url: str
    brand: str
    link: str

    class Config:
        orm_mode = True

# ----------------- ROUTES ----------------- #


@app.post("/register")
def register_route(user: UserCreate, db: Session = Depends(get_db)):
    return register(user, db)


@app.post("/token")
def login_route(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return login(form_data, db)


@app.get("/products", response_model=List[Product])
def get_products(db: Session = Depends(get_db)):
    return db.query(ProductDB).all()


@app.get("/search_products", response_model=List[Product])
def search_products(query: str, db: Session = Depends(get_db)):
    products = db.query(ProductDB).filter(
        (ProductDB.name.ilike(f"%{query}%")) |
        (ProductDB.description.ilike(f"%{query}%"))
    ).all()
    return products
