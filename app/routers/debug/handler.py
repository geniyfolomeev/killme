from fastapi import (
    APIRouter,
)


debug_handler = APIRouter(
    tags=["Debug"],
)


@debug_handler.get("/live")
@debug_handler.get("/ready")
async def health_check():
    return "OK"
