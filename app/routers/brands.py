from fastapi import APIRouter, Depends
from app.controllers.brands import select_all_brands
from app.utils.postgresql import get_session

router = APIRouter()


@router.get("/")
def get_all_brands(session=Depends(get_session)):
    all_brands = select_all_brands(session)
    return {"result": all_brands}
