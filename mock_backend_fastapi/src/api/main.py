from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

openapi_tags = [
    {
        "name": "Health",
        "description": "Basic health and readiness endpoints.",
    },
    {
        "name": "Mock",
        "description": "Mock endpoints for demonstration/testing.",
    },
]

app = FastAPI(
    title="Error Message API Mock",
    description=(
        "A minimal FastAPI mock backend exposing a single endpoint that returns a fixed error message."
    ),
    version="0.1.0",
    openapi_tags=openapi_tags,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ErrorResponse(BaseModel):
    """Response payload containing a single error string."""

    error: str = Field(..., description="Human-readable error message.")


# PUBLIC_INTERFACE
@app.get(
    "/",
    tags=["Health"],
    summary="Health check",
    description="Simple health check endpoint.",
    response_model=dict,
    operation_id="health_check",
)
def health_check() -> dict:
    """Health check endpoint.

    Returns:
        dict: `{"message": "Healthy"}` if the service is running.
    """
    return {"message": "Healthy"}


# PUBLIC_INTERFACE
@app.get(
    "/error-message",
    tags=["Mock"],
    summary="Get fixed error message",
    description='Returns the exact error: "date and time is missing".',
    response_model=ErrorResponse,
    operation_id="get_error_message",
)
def get_error_message() -> ErrorResponse:
    """Get the fixed error message used by the mock backend.

    Returns:
        ErrorResponse: Always returns `{"error": "date and time is missing"}`.
    """
    return ErrorResponse(error="date and time is missing")
