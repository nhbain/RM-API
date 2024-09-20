from fastapi import FastAPI
from mangum import Mangum
import os

app = FastAPI()

@app.get("/")
async def root():
    message = os.getenv("API_MESSAGE", "Hello Raptor Maps!")
    return {message}

handler = Mangum(app)