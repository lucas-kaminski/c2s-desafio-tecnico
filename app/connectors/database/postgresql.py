from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import POSTGRESQL_URL
from app.utils.enviroment import is_development_environment

engine = create_engine(POSTGRESQL_URL, echo=is_development_environment())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
