from fastapi import APIRouter, Header, Cookie, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from typing import Optional, List

router = APIRouter(prefix="/product", tags=["product"])

product = ["watch", "camera", "laptop"]


@router.get("/")
def get_all_product():
    # return product
    data = " ".join(product)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return {"response": response}


@router.post("/new")
def get_new_product(name: str = Form(...)):
    product.append(name)
    return product


@router.get("/withheader")
def get_products(
    response: Response,
    custom_header: Optional[List[str]] = Header(None),
    test_cookie: Optional[str] = Cookie(None),
):
    if custom_header:
        response.headers["custom_response_header"] = ", ".join(custom_header)
    return {"data": product, "custom_header": custom_header, "my_cookie": test_cookie}


@router.get(
    "/{id}",
    responses={
        200: {
            "content": {
                "text/html": {"example": "<div class = 'product'>watch</div> "}
            },
            "description": "return an HTML for product",
        },
        400: {
            "content": {"text/plain": {"example": "product not found"}},
            "description": "return an plantext message when product not found",
        },
    },
)
def get_product(id: int):
    if id > len(product):
        out = "product not found "
        return PlainTextResponse(content=out, media_type="text/plain")
    productid = product[id]
    out = f"""
    <div class = "product">{productid} </div>
    """
    return HTMLResponse(content=out, media_type="text/html")
