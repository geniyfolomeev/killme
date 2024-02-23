import grpc
from app.utils.warden.client import Warden
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from google.protobuf.descriptor_pool import DescriptorPool


async def get_grpc_handlers(service_name: str, version: str, env="stg") -> set[str]:
    version = version.replace("/", "-").lower()
    warden = Warden(service=f"{service_name}:grpc", version=version, env=env)
    host = await warden.get_endpoint()
    channel = grpc.insecure_channel(host)
    reflection_db = ProtoReflectionDescriptorDatabase(channel)
    desc_pool = DescriptorPool(reflection_db)

    handlers = set()
    for service_name in reflection_db.get_services():
        if "ServerReflection" in service_name:
            continue
        if "Cordon" in service_name:
            continue
        if "Debug" in service_name:
            continue
        service_desc = desc_pool.FindServiceByName(service_name)
        if service_desc:
            handlers.update([method.name for method in service_desc.methods])
    return handlers
