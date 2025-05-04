import logging

from app.connectors.database.postgresql import engine
from app.utils.enviroment import is_development_environment
from app.utils.postgresql import ALL_POSTGRESQL_MODELS

if not is_development_environment():
    raise EnvironmentError(
        "This script should only be run in a development environment."
    )

logger = logging.getLogger(__name__)

for model in ALL_POSTGRESQL_MODELS:
    logger.info(f"Dropping table {model.__tablename__}...")
    model.__table__.drop(engine)
