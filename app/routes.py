import logging
from fastapi import APIRouter, HTTPException, Request, Depends
from app.schemas import PredictionRequest, PredictionResponse, HealthResponse
from app.services import run_ai_prediction
from app.auth import verify_api_key
from app.config import settings

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/")
def home(request: Request):
    request_id = request.state.request_id

    logger.info(
        f"Home endpoint called | request_id={request_id}"
    )

    return {
        "message": f"{settings.APP_NAME} is running",
        "request_id": request_id
    }


@router.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="healthy",
        app_name=settings.APP_NAME,
        environment=settings.APP_ENV
    )


@router.post(
    "/predict",
    response_model=PredictionResponse,
    dependencies=[Depends(verify_api_key)]
)
def predict(request_body: PredictionRequest, request: Request):
    request_id = request.state.request_id

    logger.info(
        f"Received prediction request | request_id={request_id} | "
        f"category={request_body.category} | text_length={len(request_body.text)}"
    )

    try:
        result = run_ai_prediction(
            text=request_body.text,
            category=request_body.category,
            request_id=request_id
        )

        logger.info(
            f"Prediction response successfully generated | request_id={request_id}"
        )

        return PredictionResponse(
            input_text=request_body.text,
            category=request_body.category,
            prediction=result["prediction"],
            confidence=result["confidence"],
            request_id=request_id
        )

    except ValueError as e:
        logger.warning(
            f"Bad request | request_id={request_id} | error={str(e)}"
        )
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        logger.error(
            f"Unexpected server error | request_id={request_id} | error={str(e)}",
            exc_info=True
        )
        raise HTTPException(status_code=500, detail="Internal server error")