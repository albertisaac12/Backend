# print("Hello")

"""
POST /users HTTP/1.1
Host: localhost

Content-Type: application/json

{
    "name":"Alice"
}


Request:
Method
URL
Headers
Body

"""

"""
Response

HTTP/1.1 201 Created

Content-Type: application/json

{
    id:15,
    "name": "Alice"
}

Status Code
Headers
Body

"""


# Idempotency: A request is idempotent if making the same request multiple times has the same end result as making it once




"""
Plan

Server recevies a URL => Converts it to to short url => Sends back to User

# Server => needs to map the old url to a new one and and when cliked on new url => hits server and then rediret to the old url i.e the original one

# NEEDS a local DB that can map old and new urls


# Add in url validation as well

#   Add
"""

# Lets first explore FastAPI docs


from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

# Create an APP
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id:int, q: str | None = None):
    return {"item_id": item_id,"q":q}

@app.put("/items{item_id}")
def update_item(item_id:int,item:Item):
    return {"item_name":item.name,"item_id": item_id}


# Order for path parameters matters

"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


"""

# Similarly, you cannot redefine a path operation:
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

"""