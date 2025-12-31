from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from bson import ObjectId
from typing import Optional

from models import User, UserLogin, Task
from database import users_collection, tasks_collection
from auth import hash_password, verify_password, create_access_token

# ------------------ JWT Config ------------------
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

app = FastAPI(title="Smart ToDo API - JWT Protected")

# Enables 🔐 Authorize button in Swagger
security = HTTPBearer()


# ============= AUTH HELPERS =============
def get_current_user(credentials: security = Depends()):
    token = credentials.credentials   # Automatically extracts Bearer token

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("email")
        if not user_email:
            raise HTTPException(status_code=401, detail="Token invalid")
        return user_email

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


# ============= USER SIGNUP =============
@app.post("/signup")
def signup(user: User):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pwd = hash_password(user.password)
    users_collection.insert_one({"email": user.email, "password": hashed_pwd})
    return {"message": "Signup successfully!"}


# ============= USER LOGIN =============
@app.post("/login")
def login(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid Credentials")

    token = create_access_token({"email": user.email})
    return {"message": "Login successful", "token": token}


# ============= CREATE TASK (Protected) =============
@app.post("/tasks")
def create_task(task: Task, current_user: str = Depends(get_current_user)):
    tasks_collection.insert_one({**task.dict(), "user": current_user})
    return {"message": "Task created successfully"}


# ============= GET TASKS (Protected) =============
@app.get("/tasks")
def get_tasks(current_user: str = Depends(get_current_user)):
    tasks = list(tasks_collection.find({"user": current_user}))
    for t in tasks:
        t["_id"] = str(t["_id"])
    return tasks


# ============= UPDATE TASK (Protected) =============
@app.put("/tasks/{task_id}")
def update_task(task_id: str, task: Task, current_user: str = Depends(get_current_user)):
    tasks_collection.update_one(
        {"_id": ObjectId(task_id), "user": current_user},
        {"$set": task.dict()}
    )
    return {"message": "Task updated successfully"}


# ============= DELETE TASK (Protected) =============
@app.delete("/tasks/{task_id}")
def delete_task(task_id: str, current_user: str = Depends(get_current_user)):
    tasks_collection.delete_one({"_id": ObjectId(task_id), "user": current_user})
    return {"message": "Task deleted successfully"}
