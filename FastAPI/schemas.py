from pydantic import BaseModel, ConfigDict
from typing import List


# Used inside userdisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []

    model_config = ConfigDict(from_attributes=True)


# used inside articlesDisplay
class User(BaseModel):
    id: int
    username: str
    model_config = ConfigDict(from_attributes=True)


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creater_id: int


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    model_config = ConfigDict(from_attributes=True)
