from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi.responses import FileResponse

router = APIRouter(prefix="/file", tags=["file"])


@router.post("/")
def get_file(file: bytes = File(...)):
    content = file.decode("utf-8")
    lines = content.split("\n")
    return {"lines": lines}


@router.get("/download/{filename}", response_class=FileResponse)
def get_file(filename: str):
    path = f"files/{filename}"
    return path


@router.post("/upload")
def get_upload_file(UploadFile: UploadFile = File(...)):
    path = f"files/{UploadFile.filename}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(UploadFile.file, buffer)
    return {"filename": path, "type": UploadFile.content_type}
