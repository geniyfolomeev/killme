import uvicorn
import logging
from fastapi import (
    FastAPI,
    Request,
    HTTPException,
)
from fastapi.staticfiles import StaticFiles
from routers.collector.handler import (
    collector_handler,
)
from routers.debug.handler import (
    debug_handler,
)
from routers.main.handler import (
    main_page,
)
from routers.services.handler import (
    services_page,
)
from utils.logger import logger

app = FastAPI()
app.include_router(collector_handler)
app.include_router(debug_handler)
app.include_router(main_page)
app.include_router(services_page)
app.mount("/static", StaticFiles(directory="static"))

logging.getLogger("fastapi").disabled = True
logging.getLogger("uvicorn.access").disabled = True
logging.getLogger("uvicorn.error").disabled = True


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
