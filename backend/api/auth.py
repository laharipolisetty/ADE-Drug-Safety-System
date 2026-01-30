from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginData(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginData):
    if data.username == "admin" and data.password == "admin123":
        return {
            "token": "drug_safety_token_123",
            "role": "admin"
        }
    raise HTTPException(status_code=401, detail="Invalid credentials")
