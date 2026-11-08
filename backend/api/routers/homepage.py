from fastapi import APIRouter


router = APIRouter(prefix="", tags=["Страница \"Home page\""])

file_homepage = "index.html"


@router.get("/")
async def get_homepage():
    return {"page": "homepage"}