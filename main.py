from typing import Annotated

from fastapi import Body, FastAPI, Form, status
from pydantic import BaseModel, EmailStr, Field, StringConstraints

app = FastAPI(description="Backend for Notes QA App", title="AskNotesApp")


class UserData(BaseModel):
    email: EmailStr
    password: Annotated[str | None, StringConstraints(min_length=8, max_length=18)] = (
        Field(
            default=None, exclude=True
        )  # since exclue is true it wont be included in the model.dum()
    )
    model_config = {"extra": "forbid"}


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"Message": "Welcome to AskNotesApp, Server is up"}


# Need to learn Request Body, Database operations and Security for this to work
@app.put("/signup", status_code=status.HTTP_200_OK)
def sign_up(user_data: Annotated[UserData, Body(media_type="application/json")]):
    return {"username": user_data.email, "password": user_data.password}


@app.put("/signup2", status_code=status.HTTP_200_OK)
def sign_up_2(user_data: Annotated[UserData, Form()]):
    return {"username": user_data.email, "password": user_data.password}
