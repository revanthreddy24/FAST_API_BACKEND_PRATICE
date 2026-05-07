import logging
import time

logger = logging.getLogger(__name__)


def run_ai_prediction(text: str, category: str, request_id: str):
    start_time = time.time()

    logger.info(
        f"Starting AI prediction | request_id={request_id} | category={category}"
    )

    try:
        if not text.strip():
            logger.warning(
                f"Empty text received for prediction | request_id={request_id}"
            )
            raise ValueError("Input text cannot be empty")

        if category == "healthcare_claims":
            prediction = "Claim Denial Risk"
            confidence = 0.87

        elif category == "finance_fraud":
            prediction = "Potential Fraud"
            confidence = 0.91

        elif category == "customer_support":
            prediction = "Customer Complaint"
            confidence = 0.82

        else:
            prediction = "General Classification"
            confidence = 0.75

        model_latency = round(time.time() - start_time, 4)

        logger.info(
            f"Prediction completed | request_id={request_id} | "
            f"category={category} | prediction={prediction} | "
            f"confidence={confidence} | model_latency={model_latency}s"
        )

        return {
            "prediction": prediction,
            "confidence": confidence
        }

    except Exception as e:
        logger.error(
            f"Prediction failed | request_id={request_id} | error={str(e)}",
            exc_info=True
        )
        raise