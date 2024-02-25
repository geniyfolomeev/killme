from fastapi import (
    APIRouter,
    Request,
)
from fastapi.responses import HTMLResponse, RedirectResponse

main_page = APIRouter()


@main_page.get("/", response_class=HTMLResponse)
async def main():
    return RedirectResponse("/services")
