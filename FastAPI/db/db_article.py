from schemas import ArticleBase
from db.models import DbArticles
from sqlalchemy.orm import Session


def create_article(db: Session, request: ArticleBase):
    new_article = DbArticles(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creater_id,
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db: Session, id: int):
    article = db.query(DbArticles).filter(DbArticles.id == id).first()
    if article:
        article.user  # Ensure the user relationship is loaded
    return article
