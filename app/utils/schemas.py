from app.schemas.brands import get_all_brands_schema
from app.schemas.vehicles import get_all_vehicles_by_brand_schema

ALL_SCHEMAS = [
    get_all_brands_schema,
    get_all_vehicles_by_brand_schema,
]
