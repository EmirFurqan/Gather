from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel

class Users(BaseModel):
    username: str
    email: str
    name: str 
    surname: str 
    disabled: bool 