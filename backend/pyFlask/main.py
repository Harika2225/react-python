import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Grocery(BaseModel):
    name: str

class Groceries(BaseModel):
    groceries: List[Grocery]

app = FastAPI(debug=True)

origins = [
    "http://localhost:3000"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory_db = {"groceries" :[]}

@app.get("/groceries", response_model=Groceries)
def get_groceries():
    return Groceries(groceries=memory_db["groceries"])

@app.post("/groceries", response_model=Grocery)
def create_groceries(grocery: Grocery):
    memory_db["groceries"].append(grocery)
    return grocery

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)