from fastapi import APIRouter, Depends
from app.controllers.vehicles import select_all_vehicles_by_brand
from app.utils.postgresql import get_session

router = APIRouter()


@router.get("/")
def get_all_vehicles_by_brand(session=Depends(get_session), brand_id: int = None):
    all_vehicles = select_all_vehicles_by_brand(session, brand_id)
    return {"result": all_vehicles}
