import uvicorn
import psycopg2
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# Database Connection Setup
DATABASE_URL = "postgresql://postgres:postgres@localhost/grocery_db"

try:
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT version();")  # Check PostgreSQL version
    db_version = cur.fetchone()
    print(f"✅ Database connected successfully: {db_version[0]}")
except Exception as e:
    print(f"❌ Database connection failed: {str(e)}")
    raise SystemExit(e)  # Stop execution if DB is not connected

# Create table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS groceries (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    )
""")
conn.commit()

app = FastAPI(debug=True)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Grocery(BaseModel):
    id: int
    name: str

class GroceryCreate(BaseModel):
    name: str

@app.get("/groceries", response_model=List[Grocery])
def get_groceries():
    cur.execute("SELECT id, name FROM groceries")
    groceries = cur.fetchall()
    return [{"id": row[0], "name": row[1]} for row in groceries]

@app.post("/groceries", response_model=Grocery)
def create_grocery(grocery: GroceryCreate):
    try:
        cur.execute("INSERT INTO groceries (name) VALUES (%s) RETURNING id", (grocery.name,))
        grocery_id = cur.fetchone()[0]
        conn.commit()
        return {"id": grocery_id, "name": grocery.name}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Grocery already exists")

@app.put("/groceries/{grocery_id}", response_model=Grocery)
def update_grocery(grocery_id: int, updated_grocery: GroceryCreate):
    cur.execute("UPDATE groceries SET name = %s WHERE id = %s RETURNING id", (updated_grocery.name, grocery_id))
    if not cur.fetchone():
        conn.rollback()
        raise HTTPException(status_code=404, detail="Grocery not found")
    conn.commit()
    return {"id": grocery_id, "name": updated_grocery.name}

@app.delete("/groceries/{grocery_id}", response_model=Grocery)
def delete_grocery(grocery_id: int):
    cur.execute("DELETE FROM groceries WHERE id = %s RETURNING id, name", (grocery_id,))
    deleted_grocery = cur.fetchone()
    if not deleted_grocery:
        conn.rollback()
        raise HTTPException(status_code=404, detail="Grocery not found")
    conn.commit()
    return {"id": deleted_grocery[0], "name": deleted_grocery[1]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
