# uvicorn main:app --reload
# fastapi-venv\scripts\activate.bat
from fastapi import FastAPI
from routers import blog_get
from routers import blog_post

app = FastAPI()

app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index():
    return {"message": "Hello world"}
