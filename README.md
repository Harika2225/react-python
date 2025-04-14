# Getting Started with Hosting App

# Frontend
### `npm install -g vercel`
### `vercel login`
Next continue with GitHub, and sigup to versel, login with the OTP

### After logging in, import the required git repo and click on install

#### Now, we can create a project in versel(existing project) and click on DEPLOY

## Frontend Deployment is DONE!
## It is running in `https://fullstack-reactapp.vercel.app/`

# Backend

### Open `https://render.com/` and signup
### After signing in, click on New Web Service and authorize git,import the required git repo and click on install


# Database

### Open `https://supabase.com/` and click on start new project and authorize git, click on create new organisation and click on create new project after entering database password(postgres)
### So now we have created a project and redirected to home page

#### We can find connect at the navbar of the home page, copy the URL in backend/pyFalsk/.env
`DATABASE_URL=postgresql://postgres:[YOUR-PASSWORD]@db.ojheezbilvfmeygrvvsk.supabase.co:5432/postgres`

---------
`import os
from dotenv import load_dotenv
# Load .env file
load_dotenv()
# Get database URL
DATABASE_URL = os.getenv("DATABASE_URL")`

in terminal,
`pip install python-dotenv`
` python3 -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('DATABASE_URL'))"`

------------


## Go to Render and in environment add the key as DATABASE_URL and key as `postgresql://postgres:postgres@db.ojheezbilvfmeygrvvsk.supabase.co:5432/postgres`