from fastapi import FastAPI

app = FastAPI()

@app.post('/')
def say_hello_world():
    return "Hello World!"