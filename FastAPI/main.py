# uvicorn main:app --reload
# fastapi-venv\scripts\activate.bat
# https://www.udemy.com/course/completefastapi/?couponCode=KEEPLEARNING
# pip freeze > requirements.txt
from fastapi import FastAPI
from routers import blog_get, article
from routers import blog_post
from routers import user
from db import models
from db.database import engine

app = FastAPI()

app.include_router(article.router)
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index():
    return {"message": "Hello world"}


models.Base.metadata.create_all(engine)
