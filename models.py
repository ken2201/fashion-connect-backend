from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import uuid

# ----------------- DATABASE CONFIG ----------------- #
DATABASE_URL = "sqlite:///./products.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ----------------- PRODUCT MODEL ----------------- #


class ProductDB(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True,
                default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    price = Column(Float)
    description = Column(String)
    image_url = Column(String, nullable=True)
    brand = Column(String, index=True)
    link = Column(String, nullable=True)

# ----------------- USER MODEL ----------------- #


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True,
                default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


# ----------------- CREATE TABLES ----------------- #
Base.metadata.create_all(bind=engine)
