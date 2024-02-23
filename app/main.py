import uvicorn
from fastapi import FastAPI
from app.routers.collector.handler import (
    collector_handler,
)

app = FastAPI()
app.include_router(collector_handler)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
