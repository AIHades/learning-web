from fastapi import APIRouter


router = APIRouter(prefix="/properties", tags=["Страница \"Properties\""])

file_properties_page = ""
file_properties_daily_page = ""


@router.get("")
async def get_properties_page():
    return {"page": "properties page"}


@router.get("/properties-daily")
async def get_properties_daily_page():
    return {"page": "properties daily page"}