from fastapi import APIRouter, Depends
from fastapi.requests import Request

router = APIRouter(prefix="/dependencies", tags=["dependencies"])


def convert_params(request: Request, seperator: str):
    query = []
    for key, value in request.query_params.items():
        query.append(f"{key} {seperator} {value}")
    return query


def convert_header(
    request: Request, seperator: str = "---", query=Depends(convert_params)
):
    our_headers = []
    for key, value in request.headers.items():
        our_headers.append(f"{key}---{value}")
    return {"headers": our_headers, "query": query}


@router.get("")
def get_items(headers=Depends(convert_header)):
    return {"items": ["a", "b", "c"], "headers": headers}


class Account:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


@router.post("/")
def create_user(
    username: str, password: str, account: Account = Depends()
):  # account: Account = Depends(Account)
    return {
        "username": account.username,
        "password": account.password,
        "account": account,
    }
