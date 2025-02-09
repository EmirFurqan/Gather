from fastapi import APIRouter, HTTPException, Depends, status  # Ensure APIRouter is imported
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt, JWTError

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

SECRET_KEY = "ad69e39b5c37bbb17509cf05b164aed8b566f92a17c3da2e22cd6eaf0931456a"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class CreateUserRequest(BaseModel):
    username:str
    password:str
    
class Token(BaseModel):
    access_token:str
    token_type:str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db,
                      create_user_request:CreateUserRequest):
    create_user_model = Users(
        username=create_user_request.username,
        hashed_password= bcrypt_context.hash(create_user_request.password)
    )
    