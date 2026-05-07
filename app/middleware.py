import logging
import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        start_time = time.time()

        request.state.request_id = request_id

        logger.info(
            f"Request started | request_id={request_id} | "
            f"method={request.method} | path={request.url.path}"
        )

        try:
            response = await call_next(request)

            latency = round(time.time() - start_time, 4)

            logger.info(
                f"Request completed | request_id={request_id} | "
                f"method={request.method} | path={request.url.path} | "
                f"status_code={response.status_code} | latency={latency}s"
            )

            response.headers["X-Request-ID"] = request_id
            response.headers["X-Response-Time"] = str(latency)

            return response

        except Exception as e:
            latency = round(time.time() - start_time, 4)

            logger.error(
                f"Request failed | request_id={request_id} | "
                f"method={request.method} | path={request.url.path} | "
                f"latency={latency}s | error={str(e)}",
                exc_info=True
            )

            raise