from app.models.brand import Brand


def select_all_brands(db_session):
    return db_session.query(Brand).all()
