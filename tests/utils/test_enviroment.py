import pytest

from app.utils import enviroment


def test_get_mandatory_env_variable_set(monkeypatch):
    monkeypatch.setenv("TEST_ENV", "value")
    assert enviroment.get_mandatory_env_variable("TEST_ENV") == "value"


def test_get_mandatory_env_variable_not_set(monkeypatch):
    monkeypatch.delenv("TEST_ENV", raising=False)
    with pytest.raises(ValueError) as excinfo:
        enviroment.get_mandatory_env_variable("TEST_ENV")
    assert "Environment variable TEST_ENV is not set" in str(excinfo.value)


def test_is_development_environment_true(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "development")
    assert enviroment.is_development_environment() is True


def test_is_development_environment_false(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "production")
    assert enviroment.is_development_environment() is False
