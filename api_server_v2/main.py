from this import d
import uvicorn
from typing import Optional
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/double/{number}")
def read_item(number: int):
    return {"double": number * 2}

if __name__ == "__main__":
    PORT = os.environ.get('PORT', 8000)  # TODO: Läs detta från os.environ istället
    uvicorn.run(app, host="0.0.0.0", port=PORT)
