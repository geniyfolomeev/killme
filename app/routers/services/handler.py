from fastapi import (
    APIRouter,
    Request,
)
from fastapi.responses import HTMLResponse
from constants import templates

services_page = APIRouter()


@services_page.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    services_cov = {
        "container-processor": {
            "team": "LSSPR",
            "unit": {"value": 25.71, "changes": {"week": "+4.05", "month": "+1.03"}},
            "integration": {"value": 0, "changes": {}},
            "e2e": {"value": 33.49, "changes": {"week": "-1.36", "month": "-6.9"}}
        }, "lssms-sorting-calculator": {
            "team": "LSSMS",
            "unit": {"value": 25.71, "changes": {"week": "+0.31", "month": "-5.67", "quarter": "+10.34"}},
            "integration": {"value": 25.71, "changes": {"week": "+13.4", "month": "+29.67"}},
            "e2e": {"value": 25.71, "changes": {"week": "+0.5", "month": "+0.5"}}
        },
        "container-processor-sync": {
            "team": "LSSPR",
            "unit": {"value": 0, "changes": {}},
            "integration": {"value": 0, "changes": {}},
            "e2e": {"value": 5.32, "changes": {"week": "+5.32"}}
        }
    }
    return templates.TemplateResponse(
        "services.html",
        {"request": request, "services": services_cov, "teams": ["LSSPR", "LSSMS"]},
    )
