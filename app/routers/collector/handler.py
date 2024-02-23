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
from utils.warden.client import (
    NoEndPointException,
)
from utils.logger import logger

collector_handler = APIRouter(
    tags=["Collector"],
    prefix="/collector",
)

UPLOAD_URL = "/upload"


@collector_handler.post(UPLOAD_URL)
async def upload(request: UploadRequest = Depends(), file: UploadFile = File(...)):
    content = await file.read()
    try:
        xml = file_to_xml(content)
    except InvalidXml as e:
        logger.warning(f"POST {UPLOAD_URL} Request: {request.dict()} Error: {str(e)}")
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    try:
        handlers = await get_grpc_handlers(service_name=request.service, version=request.version, env="stg")
    except NoEndPointException as e:
        logger.warning(f"POST {UPLOAD_URL} Request: {request.dict()} Error: {str(e)}")
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    coverage = find_handlers_coverage(xml, handlers)
    logger.info(f"POST {UPLOAD_URL} Request: {request.dict()} Coverage: {coverage}")
    return coverage
