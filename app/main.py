import logging
from fastapi import FastAPI
from app.routes import router
from app.logging_config import setup_logging
from app.middleware import RequestLoggingMiddleware
from app.config import settings

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    description="Production-style AI backend with logging, middleware, API key auth, and Docker support",
    version="1.0.0"
)

app.add_middleware(RequestLoggingMiddleware)

app.include_router(router)

logger.info(
    f"{settings.APP_NAME} application started | environment={settings.APP_ENV}"
)