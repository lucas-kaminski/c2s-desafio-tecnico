from app.models.brand import Brand


def select_all_brands(db_session, name=None):
    query = db_session.query(Brand)
    if name:
        query = query.filter(Brand.name.ilike(f"%{name}%"))
    return query.all()
