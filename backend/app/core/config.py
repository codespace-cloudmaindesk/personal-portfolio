from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    """
    Application settings class.

    This class defines all configuration values required by the application,
    such as project metadata, security, database connection, CORS, and rate limiting.

    Values are automatically read from environment variables or the `.env` file.
    """

    # Project
    PROJECT_NAME: str
    VERSION: str
    API_V1_STR: str
    DEBUG: bool

    # Security
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    @field_validator("SECRET_KEY")
    @classmethod
    def validate_secret_key(cls, v: str) -> str:
        if not v or len(v) < 32:
            raise ValueError("SECRET_KEY must be at least 32 characters long")
        return v

    # Database
    DATABASE_URL: str
    DATABASE_URL_LOCAL: str

    # CORS
    BACKEND_CORS_ORIGINS: list[str]

    # Rate Limiting
    RATE_LIMIT_LOGIN: int

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
