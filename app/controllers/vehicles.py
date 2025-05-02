from app.models.color import Color
from app.models.vehicle import Vehicle


def select_all_with_filters(db_session, **filters):
    query = db_session.query(Vehicle)
    equal_filters = [
        "brand_id",
        "year",
    ]

    for key in equal_filters:
        if filters.get(key):
            query = query.filter(getattr(Vehicle, key) == filters[key])

    ilike_filters = [
        "model",
    ]
    for key in ilike_filters:
        if filters.get(key):
            query = query.filter(getattr(Vehicle, key).ilike(f"%{filters[key]}%"))

    fk_name_filters = {
        "color": "name",
        "fuel_type": "name",
        "status": "name",
    }

    for key, attr in fk_name_filters.items():
        if filters.get(key):
            query = query.join(getattr(Vehicle, key))
            query = query.filter(
                getattr(getattr(Vehicle, key).property.mapper.class_, attr).ilike(
                    f"%{filters[key]}%"
                )
            )

    all_vehicles = query.all()
    return [vehicle.to_dict() for vehicle in all_vehicles]
