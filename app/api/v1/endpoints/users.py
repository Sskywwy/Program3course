from fastapi import FastAPI, APIRouter, HTTPException, status
from typing import List, Any
from app.db.base import fake_users_db
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
def get_users():
    return list(fake_users_db.values())

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = fake_users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    new_id = len(fake_users_db) + 1
    new_user = {"id": new_id, "name": user.name, "email": user.email}
    fake_users_db[new_id] = new_user
    return new_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    del fake_users_db[user_id]
    return None

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    updated_user = {"id": user_id, "name": user.name, "email": user.email}
    fake_users_db[user_id] = updated_user
    return updated_user