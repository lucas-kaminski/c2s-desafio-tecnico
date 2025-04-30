from fastapi import APIRouter, Depends
from app.controllers.vehicles import select_all_vehicles_by_brand
from app.utils.postgresql import get_session

router = APIRouter()


@router.get("/vehicles")
def get_all_vehicles_by_brand(
    session=Depends(get_session), brand_id: int = None, model_name: str = None
):
    if not brand_id:
        return {"error": "parameter 'brand_id' is required"}
    all_vehicles = select_all_vehicles_by_brand(session, brand_id, model_name)
    return {"result": all_vehicles}
