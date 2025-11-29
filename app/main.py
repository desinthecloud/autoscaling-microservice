from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./items.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hybrid Autoscaling Demo")

class ItemCreate(BaseModel):
    name: str

class ItemOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items", response_model=List[ItemOut])
def list_items():
    db = SessionLocal()
    try:
        return db.query(Item).all()
    finally:
        db.close()

@app.post("/items", response_model=ItemOut)
def create_item(item: ItemCreate):
    db = SessionLocal()
    try:
        db_item = Item(name=item.name)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    finally:
        db.close()
