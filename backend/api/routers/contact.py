from fastapi import APIRouter


router = APIRouter(prefix="/contact", tags=["Страница \"Contact\""])

file_contacts_page = ""


@router.get("")
async def get_contacts_page():
    return {"page": "contact page"}