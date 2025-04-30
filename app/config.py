from app.utils.enviroment import get_mandatory_env_variable, is_development_environment

ENVIRONMENT = get_mandatory_env_variable("ENVIRONMENT")

OPENAI_API_KEY = get_mandatory_env_variable("OPENAI_API_KEY")

POSTGRESQL_HOST = get_mandatory_env_variable("POSTGRESQL_HOST")
POSTGRESQL_PORT = get_mandatory_env_variable("POSTGRESQL_PORT")
POSTGRESQL_USER = get_mandatory_env_variable("POSTGRESQL_USER")
POSTGRESQL_PASSWORD = get_mandatory_env_variable("POSTGRESQL_PASSWORD")
POSTGRESQL_DATABASE_NAME = get_mandatory_env_variable("POSTGRESQL_DATABASE_NAME")

SERVER_HOST = get_mandatory_env_variable("SERVER_HOST")
SERVER_PORT = get_mandatory_env_variable("SERVER_PORT")
SERVER_URL = f"{'http' if is_development_environment() else 'https'}://{SERVER_HOST}:{SERVER_PORT}"


POSTGRESQL_URL = f"postgresql://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_DATABASE_NAME}"
