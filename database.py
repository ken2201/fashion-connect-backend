# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL (SQLite)
DATABASE_URL = "sqlite:///./products.db"

# Engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
