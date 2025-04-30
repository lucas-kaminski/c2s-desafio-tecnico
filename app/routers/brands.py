from fastapi import APIRouter, Depends
from app.controllers.brands import select_all_brands
from app.utils.postgresql import get_session

router = APIRouter()


@router.get("/brands")
def get_all_brands(session=Depends(get_session), name: str = None):
    all_brands = select_all_brands(session, name)
    return {"result": all_brands}
