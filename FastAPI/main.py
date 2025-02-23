# uvicorn main:app --reload
# fastapi-venv\scripts\activate.bat
# https://www.udemy.com/course/completefastapi/?couponCode=KEEPLEARNING
# pip freeze > requirements.txt
from fastapi import FastAPI, status, HTTPException
from routers import blog_get, article
from routers import blog_post
from routers import user
from routers import product
from auth import authentication
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(authentication.router)
app.include_router(article.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index():
    return {"message": "Hello world"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={"detail": exc.message})


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: HTTPException):
#     return PlainTextResponse(str(exc), status_code=404)


models.Base.metadata.create_all(engine)

origins = ["http://localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
