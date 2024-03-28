from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "We Love Datascientest, and we did it again and again! We build a new complete release CI/CD Pipeline !!"  + 2}
