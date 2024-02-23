import uvicorn
from fastapi import (
    FastAPI,
    Request,
    HTTPException,
)
from routers.collector.handler import (
    collector_handler,
)
from routers.debug.handler import (
    debug_handler,
)
from utils.logger import logger

app = FastAPI()
app.include_router(collector_handler)
app.include_router(debug_handler)


@app.middleware("http")
async def log(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        if not isinstance(e, HTTPException):
            logger.critical(f"{request.method} {request.url.path} ERROR: {e}")
        raise e

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
