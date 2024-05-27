from fastapi import FastAPI
from api.private import get_options_chain, options_algo

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.get("/api/test")
def test():
    return {"message": "Test"}

@app.get('/api/get_expirations')
def get_expirations():
    # data = request.json
    # ticker = data['ticker']
    return get_options_chain.get_expirations('AAPL')