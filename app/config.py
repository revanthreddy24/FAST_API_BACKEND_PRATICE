import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI AI Backend")
    APP_ENV: str = os.getenv("APP_ENV", "development")
    API_KEY: str = os.getenv("API_KEY", "default-dev-key")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()