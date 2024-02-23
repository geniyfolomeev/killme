from pydantic import BaseModel
from typing import (
    Literal
)


class UploadRequest(BaseModel):
    platform: Literal["go", "dotnet"]
    service: str
    version: str
    type: Literal["unit", "integration", "e2e"]
