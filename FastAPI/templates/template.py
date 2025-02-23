from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from custom_log import log
from fastapi import BackgroundTasks

router = APIRouter(prefix="/template",tags=["template"])
templates = Jinja2Templates(directory="templates")

@router.get("/products/{id}", response_class = HTMLResponse)
def get_product(id: str,request: Request, bt:BackgroundTasks):
    bt.add_task(log_template_call,f"get_Product function was called with {id}")
    return templates.TemplateResponse("product.html",{"request":request,"id":id})


def log_template_call(message:str):
    log("MYAPI",message)
