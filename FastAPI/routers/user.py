from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from schemas import UserBase, UserDisplay
from typing import List
from auth.oauth2 import get_current_user

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


@router.get("/", response_model=List[UserDisplay])
def get_all_user(
    db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)
):
    return db_user.get_all_user(db)


@router.get("/{id}", response_model=UserDisplay)
def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return db_user.get_user(db, id)


@router.post("/{id}/update")
def update_user(
    id: int,
    request: UserBase,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return db_user.update_user(db, id, request)


@router.get("/{id}/delete")
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return db_user.delete_user(db, id)
