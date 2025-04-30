from app.models.vehicle import Vehicle


def select_all_vehicles_by_brand(db_session, brand_id, model_name=None):
    vehicles = db_session.query(Vehicle).filter(Vehicle.brand_id == brand_id)
    if model_name:
        vehicles = vehicles.filter(Vehicle.model.ilike(f"%{model_name}%"))
    vehicles = vehicles.all()
    return [vehicle.to_dict() for vehicle in vehicles]
