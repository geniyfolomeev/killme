"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from abc import (
    ABCMeta,
    abstractmethod,
)

from grpc import (
    Channel,
    Server,
    ServicerContext,
    UnaryStreamMultiCallable,
)

from typing import (
    Iterator,
)

from ozbalance.warden.stubs.warden.discovery.v1.discovery_pb2 import (
    MeshInfoRequest,
    MeshInfoResponse,
    NeighboursRequest,
    NeighboursResponse,
)


class DiscoveryServiceStub:
    def __init__(self, channel: Channel) -> None: ...
    Neighbours: UnaryStreamMultiCallable[
        NeighboursRequest,
        NeighboursResponse]

    MeshInfo: UnaryStreamMultiCallable[
        MeshInfoRequest,
        MeshInfoResponse]


class DiscoveryServiceServicer(metaclass=ABCMeta):
    @abstractmethod
    def Neighbours(self,
        request: NeighboursRequest,
        context: ServicerContext,
    ) -> Iterator[NeighboursResponse]: ...

    @abstractmethod
    def MeshInfo(self,
        request: MeshInfoRequest,
        context: ServicerContext,
    ) -> Iterator[MeshInfoResponse]: ...


def add_DiscoveryServiceServicer_to_server(servicer: DiscoveryServiceServicer, server: Server) -> None: ...
