from sqlalchemy.orm import Session
from db.models import DbUser
from db.hash import Hash
from schemas import UserBase
from fastapi import HTTPException, status


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_user(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f" user with {id} not found"
        )
    return user


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f" user with username: {username} not found",
        )
    return user


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with {id} not found for updation",
        )
    user.update(
        {
            DbUser.email: request.email,
            DbUser.username: request.username,
            DbUser.password: Hash.bcrypt(request.password),
        }
    )
    db.commit()
    return "ok"


def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with {id} not found for Deletion",
        )
    db.delete(user)
    db.commit()
    return "ok"
