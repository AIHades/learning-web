from fastapi import APIRouter


router = APIRouter(prefix="/about-us", tags=["Страница \"About us\""])

file_about_us_page = ""


@router.get("")
async def get_about_us_page():
    return {"page": "about us page"}