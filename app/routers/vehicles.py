from typing import Optional

from fastapi import APIRouter, Depends, Query

from app.controllers.vehicles import select_all_with_filters
from app.utils.postgresql import get_session

router = APIRouter()


@router.get("/vehicles", tags=["vehicles"])
def get_vehicles(
    brand_id: int,
    model: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    color: Optional[str] = Query(None),
    fuel_type: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    session=Depends(get_session),
):
    filters = {
        "brand_id": brand_id,
        "year": year,
        "model": model,
        "color": color,
        "fuel_type": fuel_type,
        "status": status,
    }
    all_vehicles = select_all_with_filters(session, **filters)
    return {"result": all_vehicles}
