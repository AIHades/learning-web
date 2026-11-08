from fastapi import APIRouter


router = APIRouter(prefix="/services", tags=["Страница \"Services\""])

file_services_page = ""


@router.get("")
async def get_services_page():
    return {"page": "services page"}