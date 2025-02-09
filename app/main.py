from fastapi import Depends, FastAPI, HTTPException, status
from typing import List
from pydantic import BaseModel
import auth



app = FastAPI()
app.include_router(auth.router)

