from app.models.vehicle import Vehicle


def select_all_vehicles_by_brand(db_session, brand_id):
    if not brand_id:
        return []

    vehicles = db_session.query(Vehicle).filter(Vehicle.brand_id == brand_id).all()
    return [vehicle.to_dict() for vehicle in vehicles]
