from fastapi import FastAPI
from pydantic import BaseModel
import os
import subprocess

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():

    subprocess.call("python test_network.py --model santa_not_santa.model --image examples/318a96d591df06f88e22eb4a004c3a_gallery.jpg  > out.txt", shell=True)
    file_variable = open('out.txt')
    all_lines_variable = file_variable.readlines()
    result = all_lines_variable[2 - 1]
    proba = all_lines_variable[3 - 1]

    return {"Result": result, "Accuracy": proba}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}





