import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Database connection string
# DATABASE_URL = "postgresql://postgres:postgres@localhost/grocery_db"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Model
class GroceryDB(Base):
    __tablename__ = "groceries"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)

# Create table if not exists
Base.metadata.create_all(bind=engine)

# Pydantic Models
class Grocery(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # Allows ORM conversion

class GroceryCreate(BaseModel):
    name: str

# FastAPI App
app = FastAPI(debug=True)

# CORS Configuration
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get All Groceries
@app.get("/groceries", response_model=list[Grocery])
def get_groceries(db: Session = Depends(get_db)):
    return db.query(GroceryDB).all()

# Create a New Grocery
@app.post("/groceries", response_model=Grocery)
def create_grocery(grocery: GroceryCreate, db: Session = Depends(get_db)):
    new_grocery = GroceryDB(name=grocery.name)
    db.add(new_grocery)
    db.commit()
    db.refresh(new_grocery)
    return new_grocery

# Update a Grocery
@app.put("/groceries/{grocery_id}", response_model=Grocery)
def update_grocery(grocery_id: int, updated_grocery: GroceryCreate, db: Session = Depends(get_db)):
    grocery = db.query(GroceryDB).filter(GroceryDB.id == grocery_id).first()
    if not grocery:
        raise HTTPException(status_code=404, detail="Grocery not found")
    grocery.name = updated_grocery.name
    db.commit()
    db.refresh(grocery)
    return grocery

# Delete a Grocery
@app.delete("/groceries/{grocery_id}", response_model=Grocery)
def delete_grocery(grocery_id: int, db: Session = Depends(get_db)):
    grocery = db.query(GroceryDB).filter(GroceryDB.id == grocery_id).first()
    if not grocery:
        raise HTTPException(status_code=404, detail="Grocery not found")
    db.delete(grocery)
    db.commit()
    return grocery

# Run FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
