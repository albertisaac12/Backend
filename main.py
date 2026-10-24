from typing import Annotated

from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr, Field, StringConstraints

app = FastAPI(description="Backend for Notes QA App", title="AskNotesApp")


class UserData(BaseModel):
    email: EmailStr
    password: Annotated[str | None, StringConstraints(min_length=8, max_length=18)] = (
        Field(default=None)
    )


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"Message": "Welcome to AskNotesApp, Server is up"}


# Need to learn Request Body, Database operations and Security for this to work
@app.get("/signup", status_code=status.HTTP_200_OK)
def sign_up(user_data: UserData):
    pass
