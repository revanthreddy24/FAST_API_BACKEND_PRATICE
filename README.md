echo "# FastAPI AI Backend

A production-style FastAPI backend for AI prediction workflows with request validation, logging, middleware, API-key authentication, health checks, and Docker support.

## Features

- FastAPI REST API
- POST /predict endpoint
- Request/response validation with Pydantic
- File-based logging with log rotation
- Request ID and latency tracking middleware
- API key authentication
- Health check endpoint
- Docker support

## Project Structure

\`\`\`
fastapi-ai-backend/
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── services.py
│   ├── schemas.py
│   ├── middleware.py
│   ├── logging_config.py
│   ├── config.py
│   └── auth.py
├── logs/
├── .env.example
├── Dockerfile
├── requirements.txt
└── README.md
\`\`\`

## Setup

\`\`\`bash
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
\`\`\`

Open Swagger UI:

\`\`\`
http://127.0.0.1:8000/docs
\`\`\`

## Environment Variables

\`\`\`env
APP_NAME=FastAPI AI Backend
APP_ENV=development
API_KEY=replace-with-your-api-key
LOG_LEVEL=INFO
\`\`\`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Home |
| GET | /health | Health check |
| POST | /predict | Protected AI prediction endpoint |

## Example Request

Header:

\`\`\`
x-api-key: your-api-key
\`\`\`

Body:

\`\`\`json
{
  \"text\": \"Patient claim was denied due to missing provider information\",
  \"category\": \"healthcare_claims\"
}
\`\`\`

## Docker

\`\`\`bash
docker build -t fastapi-ai-backend .
docker run -p 8000:8000 --env-file .env fastapi-ai-backend
\`\`\`

## Tech Stack

FastAPI, Python, Pydantic, Uvicorn, Docker, Logging
" > README.md
