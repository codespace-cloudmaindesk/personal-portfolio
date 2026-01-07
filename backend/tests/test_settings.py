import pytest
from app.core.config import Settings

ENV_VARS = {
    "PROJECT_NAME": "Test API",
    "VERSION": "1.0.0",
    "API_V1_STR": "/api/v1",
    "DEBUG": "true",
    "SECRET_KEY": "supersecret",
    "ALGORITHM": "HS256",
    "ACCESS_TOKEN_EXPIRE_MINUTES": "30",
    "REFRESH_TOKEN_EXPIRE_DAYS": "7",
    "DATABASE_URL": "sqlite:///./test.db",
    "DATABASE_URL_LOCAL": "sqlite:///./test_local.db",
    "BACKEND_CORS_ORIGINS": '["http://localhost:3000","http://localhost:5173"]',
    "RATE_LIMIT_LOGIN": "5",
}


def test_settings_load(monkeypatch):
    for k, v in ENV_VARS.items():
        monkeypatch.setenv(k, v)
    settings = Settings()
    assert settings.PROJECT_NAME == "Test API"
    assert settings.DEBUG is True
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES == 30
    assert settings.BACKEND_CORS_ORIGINS == [
        "http://localhost:3000",
        "http://localhost:5173",
    ]


def test_missing_required_field(monkeypatch):
    # Patch model_config to ignore .env file
    current_config = Settings.model_config.copy()
    current_config["env_file"] = ".nonexistent"
    monkeypatch.setattr(Settings, "model_config", current_config)

    for k in ENV_VARS.keys():
        monkeypatch.delenv(k, raising=False)
    with pytest.raises(Exception):
        Settings()
