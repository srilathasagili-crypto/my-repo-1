from fastapi import FastAPI
from app import add, subtract, multiply

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My first CI/CD application"}

@app.get("/add/{a}/{b}")
def addition(a: int, b: int):
    return {"result": add(a, b)}

@app.get("/subtract/{a}/{b}")
def subtraction(a: int, b: int):
    return {"result": subtract(a, b)}

@app.get("/multiply/{a}/{b}")
def multiplication(a: int, b: int):
    return {"result": multiply(a, b)}