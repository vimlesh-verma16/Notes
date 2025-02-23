from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from schemas import ArticleBase, ArticleDisplay
from auth.oauth2 import get_current_user
from schemas import UserBase

router = APIRouter(prefix="/article", tags=["article"])


# create_article is dependent on user id if user id is not their it will give error
@router.post("/", response_model=ArticleDisplay)
def create_article(
    request: ArticleBase,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return {"data": db_article.create_article(db, request)}


# get specific article
@router.get("/{id}")  # , response_model=ArticleDisplay
def get_article(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user),
):
    return {"data": db_article.get_article(db, id), "current_user": current_user}
