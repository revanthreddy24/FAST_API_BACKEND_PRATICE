import logging
import os
from logging.handlers import RotatingFileHandler
from app.config import settings


def setup_logging():
    os.makedirs("logs", exist_ok=True)

    log_file_path = "logs/app.log"

    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=5 * 1024 * 1024,
        backupCount=3
    )

    console_handler = logging.StreamHandler()

    log_format = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(log_format)
    console_handler.setFormatter(log_format)

    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)

    logging.basicConfig(
        level=log_level,
        handlers=[
            file_handler,
            console_handler
        ]
    )