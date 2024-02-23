import uvicorn
from fastapi import FastAPI
from routers.collector.handler import (
    collector_handler,
)
from routers.debug.handler import (
    debug_handler,
)

app = FastAPI()
app.include_router(collector_handler)
app.include_router(debug_handler)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
