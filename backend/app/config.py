from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./hirevium.db"

    # JWT
    JWT_SECRET: str = "hirevium-super-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # Google Gemini
    GOOGLE_API_KEY: str = "your-gemini-api-key-here"
    GEMINI_API_KEY: str | None = None

    # Server
    BACKEND_PORT: int = 8000
    FRONTEND_URL: str = "http://localhost:3001"

    # Uploads
    UPLOAD_DIR: str = "./uploads"

    model_config = {"env_file": ".env", "extra": "ignore"}


@lru_cache()
def get_settings() -> Settings:
    return Settings()
