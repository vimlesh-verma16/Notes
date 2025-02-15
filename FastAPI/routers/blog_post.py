from enum import Enum
from typing import Optional, List
from pydantic import BaseModel
from fastapi import APIRouter, status, Response, Query, Body, Path

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogModel(BaseModel):
    title: str
    content: str
    number_of_comments: int
    published: Optional[bool]


# Combinening all three data types
@router.post("/new/{id}")
def create_blog(
    blog: BlogModel, id: int, version: int
):  # id is path parameter, version is query parameter, blog is request body parameter
    return {"id": id, "data": blog, "version": version}


# The class BlogModel inherits from BaseModel, which means it will automatically validate incoming data against the defined fields.
# In the create_post function, blog: BlogModel automatically converts and validates incoming JSON data to ensure it adheres to BlogModel.


@router.post("/new/{id}/comment/{comment_id}")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(
        None,
        title="title of the comment",
        description="Detail of comment",
        alias="commentTitle",
        deprecated=True,
    ),
    content: str = Body(..., min_length=10),
    version: Optional[List[str]] = Query(
        None
    ),  # content: str = Body(...) this is mandatory attribute
    comment_id: int = Path(..., gt=5, le=10),
):
    return {
        "id": id,
        "blog": blog,
        "comment_id": comment_id,
        "content": content,
        "version": version,
        "comment_title": comment_title,
    }
