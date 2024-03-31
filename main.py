from fastapi import FastAPI, HTTPException
from db import create_db_and_tables
from model import *

app = FastAPI()

# Call the function to create the database and tables when starting the application
create_db_and_tables()

@app.get("/")
def root():
    return {"message": "Fast API in Python"}
