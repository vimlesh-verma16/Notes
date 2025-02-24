# uvicorn main:app --reload
# fastapi-venv\scripts\activate.bat
# https://www.udemy.com/course/completefastapi/?couponCode=KEEPLEARNING
# pip freeze > requirements.txt
from fastapi import FastAPI
from routers import blog_get, article
from routers import blog_post
from routers import user
from routers import product
from routers import file, dependencies
from templates import template
from auth import authentication
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import time
from fastapi.responses import HTMLResponse
from client import html
from fastapi.websockets import WebSocket


app = FastAPI()

app.include_router(authentication.router)
app.include_router(dependencies.router)
app.include_router(template.router)
app.include_router(file.router)
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


@app.get("/")
async def get():
    return HTMLResponse(content=html)


clients = []


@app.websocket("/chats")
async def websocket_endpoints(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: HTTPException):
#     return PlainTextResponse(str(exc), status_code=404)


models.Base.metadata.create_all(engine)

origins = ["http://localhost:3000"]


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers["duration"] = str(duration)
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/files", StaticFiles(directory="files"), name="files")
