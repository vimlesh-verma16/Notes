from enum import Enum
from typing import Optional

from fastapi import FastAPI, status, Response

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello world"}


# order is import hardcoded path should come first so it starts matching from the first path to last and in the end the generic one should come like {id}
# @app.get("/blog/all")
# def get_blogs_at_value():
#     return {"message": "All blogs provided"}


@app.get(
    "/blog/all",
    tags=["blog"],
    summary="Retrevies all blogs",
    description="This api call simulates fetching all blogs",
)
def get_all_blogs(
    page=1, page_size: Optional[int] = None
):  # query parameter are page and page size default with optional parameter
    return {"message": f"All page size {page_size} on page {page}"}


@app.get(
    "/blog/{id}/comment/{comment_id}", tags=["blog", "comment"]
)  # Combined path parameter with query parameter
def get_comments(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    """Get comments for a specific blog and comment.

    This endpoint retrieves comments based on the provided blog ID and comment ID.
    It also accepts optional query parameters for validation and username.

    Args:

        -  id (int): The ID of the blog.
        -  comment_id (int): The ID of the comment.
        -  valid (bool, optional): A flag indicating whether the comment is valid. Defaults to True.
        -  username (Optional[str], optional): The username associated with the comment. Defaults to None.
    """
    return {
        "message": f"blog id:{id}, comment: {comment_id}, valid: {valid},username: {username} "
    }


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/blog/type/{type}", tags=["blog"])  # Use when you have a predefined path
def get_blog_type(type: BlogType):  # Pass the Enum that you have defined
    return {"message": f"blog type is: {type}"}


@app.get("/blog/{id}", status_code=status.HTTP_200_OK, tags=["blog"])
def get_blog(id: int, response: Response):  # type validation for path parameter in int
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"blog id:{id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"blog with id: {id}"}


@app.get("/blog/{at}/{value}", tags=["blog"])
def get_blogs_at_value(value: int, at=1):
    return {"message": f"the blog at {at} and the value is {value}"}
