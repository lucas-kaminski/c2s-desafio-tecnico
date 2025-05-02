import os


def get_mandatory_env_variable(name):
    if os.getenv("SKIP_ENV_CHECK") == "True":
        return "PYTEST_SKIP_ENV_CHECK"

    value = os.getenv(name)
    if not value:
        raise ValueError(f"Environment variable {name} is not set")
    return value


def is_development_environment():
    return get_mandatory_env_variable("ENVIRONMENT") == "development"
