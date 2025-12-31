from pydantic import BaseModel, EmailStr
from typing import Optional

# User Schema for Signup
class User(BaseModel):
    email: EmailStr
    password: str

# User Schema for Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Task Schema
class Task(BaseModel):
    title: str
    description: Optional[str] = ""
    completed: Optional[bool] = False
