# Getting Started with Python App

In backend directory, run the following to install the required dependencies

### `pip install -r pyFlask/requirements.txt`

In pyFlask directory, run the following to install the required dependencies

### `python3 main.py`

Or directly in pyFlask,

### `pip install -r requireements.txt`
### `python3 main.py` or ` uvicorn main:app --reload`

If Database connection is failed,
### `pg_isready -h localhost -U your_username -d grocery_db`

if you see, 
#### localhost:5432 - accepting connections
it means connected, if it fails, start postgresql
#### `sudo systemctl start postgresql`

To check FastAPI server is working fine, run the command to check,

#### `curl -X GET "http://localhost:8000/groceries"`

if it fails, it means DB is running, but the FastAPI server isn't running or not accessible.

Switch to PostgreSQL User
#### `sudo -i -u postgres`

Open PostgreSQL Shell
#### `psql`
Create the Database
#### `CREATE DATABASE grocery_db;`
Exit PostgreSQL
#### `\q`

Verify the Database Exists
#### `psql -U postgres -l`

Try Connecting Again
#### `psql -U postgres -d grocery_db -h localhost`

Now run again `python3 main.py`