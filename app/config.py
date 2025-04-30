from app.utils.enviroment import get_mandatory_env_variable

POSTGRESQL_HOST = get_mandatory_env_variable("POSTGRESQL_HOST")
POSTGRESQL_PORT = get_mandatory_env_variable("POSTGRESQL_PORT")
POSTGRESQL_USER = get_mandatory_env_variable("POSTGRESQL_USER")
POSTGRESQL_PASSWORD = get_mandatory_env_variable("POSTGRESQL_PASSWORD")
POSTGRESQL_DATABASE_NAME = get_mandatory_env_variable("POSTGRESQL_DATABASE_NAME")

POSTGRESQL_URL = f"postgresql://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_DATABASE_NAME}"
