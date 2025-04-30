import os


def get_mandatory_env_variable(name):
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Environment variable {name} is not set")
    return value
