from typing import Union
#Union -> Variable can be of different types String or none

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"Everything is ok with API till here"}