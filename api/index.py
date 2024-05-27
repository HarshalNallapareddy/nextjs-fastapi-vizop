from fastapi import FastAPI
from api.private import get_options_chain, options_algo

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.get("/api/test")
def test():
    return {"message": "Test"}