from typing import Union
#Union -> Variable can be of different types String or none

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"Everything is ok with API till here"}

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Union[str,None] = None):
    return {"item_id":item_id, "query":q}

@app.get("/student/{student_id}")
def get_student(student_id: int, q:Union[str, None] = None):
    return {"Student Id is :":student_id, "Query is":q}