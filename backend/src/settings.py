"""Base settings for the project."""
from pydantic import BaseSettings

_DEFAULT_ENV_FILE = ".env"


class Settings(BaseSettings):
    """Base settings for the module."""

    DATABASE_URL: str
    PREFIX_URL: str = ""

    class Config:
        """Env file format and path."""

        env_file = _DEFAULT_ENV_FILE
        env_file_encoding = "utf-8"


settings = Settings()
