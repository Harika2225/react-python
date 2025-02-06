import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Grocery(BaseModel):
    id: int # Unique identifier for each grocery to update and del
    name: str

class GroceryCreate(BaseModel):
    name: str # No ID required in request

app = FastAPI(debug=True)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory_db: List[Grocery] = []
next_id = 0  # Counter to track the next available ID

@app.get("/groceries", response_model=List[Grocery])
def get_groceries():
    return memory_db  # Returns list with `id` and `name`

@app.post("/groceries", response_model=Grocery)
def create_grocery(grocery: GroceryCreate):
    global next_id
    new_grocery = Grocery(id=next_id, name=grocery.name)  # Assign sequential ID
    memory_db.append(new_grocery)
    next_id += 1  # Increment counter for next grocery
    return new_grocery

@app.put("/groceries/{grocery_id}", response_model=Grocery)
def update_grocery(grocery_id: int, updated_grocery: GroceryCreate):
    for grocery in memory_db:
        if grocery.id == grocery_id:
            grocery.name = updated_grocery.name
            return grocery
    raise HTTPException(status_code=404, detail="Grocery not found")

@app.delete("/groceries/{grocery_id}", response_model=Grocery)
def delete_grocery(grocery_id: int):
    global memory_db
    for i, grocery in enumerate(memory_db):
        if grocery.id == grocery_id:
            return memory_db.pop(i)
    raise HTTPException(status_code=404, detail="Grocery not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
