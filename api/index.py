from fastapi import FastAPI, Request
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

@app.get('/api/get_strikes')
async def get_strikes(request: Request):
    data = await request.json()
    print(data)
    ticker = data['ticker']
    expiration = data['expiration']
    return get_options_chain.get_strikes(ticker, expiration)