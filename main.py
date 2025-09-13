from typing import Union
#Union -> Variable can be of different types String or none

from fastapi import FastAPI
# FastAPI to run the apis 

from pydantic import BaseModel
# pydantic gives us data validation via models

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    is_offer: Union[bool,None] = None


# -------- GET Requests --------------
@app.get("/")
def read_root():
    return{"message":"Everything is ok with API till here"}

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Union[str,None] = None):
    return {"item_id":item_id, "query":q}

@app.get("/student/{student_id}")
def get_student(student_id: int, q:Union[str, None] = None):
    return {"Student Id is :":student_id, "Query is":q}

# ---------- PUT Request -----------------

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item.is_offer == True :
        offer= "Is on Offer"
    else:
        offer= "Is not in offer"
    return {"Item Id is": item_id, "Item name": item.name, "Is on sale?" : item.is_offer, "Offer": offer}

