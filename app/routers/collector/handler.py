from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException,
)
from .xml_parser import (
    file_to_xml,
    find_handlers_coverage,
    InvalidXml,
)
from .models import (
    UploadRequest,
)
from .grpc_helper import (
    get_grpc_handlers,
)
from app.utils.warden.client import (
    NoEndPointException,
)

collector_handler = APIRouter(
    tags=["Collector"],
    prefix="/collector",
)


@collector_handler.post("/upload")
async def upload(request: UploadRequest = Depends(), file: UploadFile = File(...)):
    content = await file.read()
    try:
        xml = file_to_xml(content)
    except InvalidXml as e:
        return HTTPException(
            status_code=400,
            detail=str(e),
        )

    try:
        handlers = await get_grpc_handlers(service_name=request.service, version=request.version, env="stg")
    except NoEndPointException as e:
        return HTTPException(
            status_code=400,
            detail=str(e)
        )

    coverage = find_handlers_coverage(xml, handlers)

    return coverage
