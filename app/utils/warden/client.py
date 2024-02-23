import grpc
from app.constants import WARDEN_HOST_TEMPLATE
from app.utils.warden.stubs.endpoints.v1.endpoints_pb2_grpc import (
    EndpointsServiceStub,
)
from app.utils.warden.stubs.endpoints.v1.endpoints_pb2 import GetEndpointsRequest


class NoEndPointException(Exception):
    pass


class Warden:
    def __init__(self, env: str, service: str, version: str = "master"):
        self.service = service
        self.version = version
        self.env = env
        self.channel = grpc.aio.insecure_channel(WARDEN_HOST_TEMPLATE.format(env=env))

    async def get_endpoint(self) -> str:
        stub = EndpointsServiceStub(self.channel)
        response = await stub.GetEndpoints(
            GetEndpointsRequest(service=self.service)
        )
        for item in response.endpoints:
            is_default_route = item.attributes.get('isDefaultRoute')
            if item.attrs.version != self.version and self.env != "prod":
                if not (is_default_route and self.version == 'master'):
                    continue
            return item.address
        raise NoEndPointException(f'Не удалось получить адрес для сервиса {self.service} с версией {self.version}')
