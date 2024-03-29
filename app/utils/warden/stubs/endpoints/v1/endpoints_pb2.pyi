"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from builtins import (
    bool,
    int,
    type,
)

from google.protobuf.descriptor import (
    Descriptor,
    EnumDescriptor,
    FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer,
    ScalarMap,
)

from google.protobuf.internal.enum_type_wrapper import (
    EnumTypeWrapper,
)

from google.protobuf.message import (
    Message,
)

from ozbalance.warden.stubs.google.protobuf.timestamp_pb2 import (
    Timestamp,
)

from ozbalance.warden.stubs.google.protobuf.wrappers_pb2 import (
    UInt32Value,
)

from typing import (
    Iterable,
    Mapping,
    NewType,
    Optional,
    Text,
)

from typing_extensions import (
    Literal,
    TypeAlias,
)


DESCRIPTOR: FileDescriptor


_AttributeLabels: _AttributeLabels

class _AttributeLabels:
    ValueType = NewType('ValueType', int)
    V: TypeAlias = ValueType

_AttributeLabelsEnumTypeWrapper: _AttributeLabelsEnumTypeWrapper

class _AttributeLabelsEnumTypeWrapper(EnumTypeWrapper[_AttributeLabels.ValueType], type):
    DESCRIPTOR: EnumDescriptor
    version: _AttributeLabels.ValueType  # 0
    """version is attribute name to hold endpoint version."""

    isDefaultRoute: _AttributeLabels.ValueType  # 1
    """isDefaultRoute is attribute name to hold if endpoint is in the defaultRoute."""

    weight: _AttributeLabels.ValueType  # 2
    """weight is attribute name to hold weight of a version to balance traffic to."""

    role: _AttributeLabels.ValueType  # 4
    """role is attribute name to hold current role of a Patroni-cluster replica. Values are next:

    - master
    - sync
    - async
    """


AttributeLabels: AttributeLabels

class AttributeLabels(_AttributeLabels, metaclass=_AttributeLabelsEnumTypeWrapper):
    """Internal keys that returns in Endpoint.attributes."""
    pass

version: AttributeLabels.ValueType  # 0
"""version is attribute name to hold endpoint version."""

isDefaultRoute: AttributeLabels.ValueType  # 1
"""isDefaultRoute is attribute name to hold if endpoint is in the defaultRoute."""

weight: AttributeLabels.ValueType  # 2
"""weight is attribute name to hold weight of a version to balance traffic to."""

role: AttributeLabels.ValueType  # 4
"""role is attribute name to hold current role of a Patroni-cluster replica. Values are next:

- master
- sync
- async
"""



_BalancerName: _BalancerName

class _BalancerName:
    ValueType = NewType('ValueType', int)
    V: TypeAlias = ValueType

_BalancerNameEnumTypeWrapper: _BalancerNameEnumTypeWrapper

class _BalancerNameEnumTypeWrapper(EnumTypeWrapper[_BalancerName.ValueType], type):
    DESCRIPTOR: EnumDescriptor
    ozwrredf: _BalancerName.ValueType  # 0
    """ozwrredf is a balancer name that impelements EDF scheduling for WRR algorithm.
    Deprecated and will be removed in next versions
    """

    o3_wrr: _BalancerName.ValueType  # 2
    o3_rnd: _BalancerName.ValueType  # 3
    o3_p2c: _BalancerName.ValueType  # 4
    o3_p2c_lc: _BalancerName.ValueType  # 5
    o3_p2c_md: _BalancerName.ValueType  # 6
    o3_chash: _BalancerName.ValueType  # 8
    """consistent hashing for short"""

    o3_p2c_ewma: _BalancerName.ValueType  # 9

BalancerName: BalancerName

class BalancerName(_BalancerName, metaclass=_BalancerNameEnumTypeWrapper):
    """Internal names that allows to manupulate with balancers implementations."""
    pass

ozwrredf: BalancerName.ValueType  # 0
"""ozwrredf is a balancer name that impelements EDF scheduling for WRR algorithm.
Deprecated and will be removed in next versions
"""

o3_wrr: BalancerName.ValueType  # 2
o3_rnd: BalancerName.ValueType  # 3
o3_p2c: BalancerName.ValueType  # 4
o3_p2c_lc: BalancerName.ValueType  # 5
o3_p2c_md: BalancerName.ValueType  # 6
o3_chash: BalancerName.ValueType  # 8
"""consistent hashing for short"""

o3_p2c_ewma: BalancerName.ValueType  # 9


_LoadBalancingStrategy: _LoadBalancingStrategy

class _LoadBalancingStrategy:
    ValueType = NewType('ValueType', int)
    V: TypeAlias = ValueType

_LoadBalancingStrategyEnumTypeWrapper: _LoadBalancingStrategyEnumTypeWrapper

class _LoadBalancingStrategyEnumTypeWrapper(EnumTypeWrapper[_LoadBalancingStrategy.ValueType], type):
    DESCRIPTOR: EnumDescriptor
    wrr: _LoadBalancingStrategy.ValueType  # 0
    """Weighted round robin"""

    random: _LoadBalancingStrategy.ValueType  # 1
    """Random"""

    consthash: _LoadBalancingStrategy.ValueType  # 2
    """Consistent hashing"""

    p2c: _LoadBalancingStrategy.ValueType  # 3
    """Power of 2 choices"""

    p2clc: _LoadBalancingStrategy.ValueType  # 4
    """p2c with least connections (default for p2c strategy)"""

    p2crt: _LoadBalancingStrategy.ValueType  # 5
    """p2c with response time load adviser"""

    p2cmd: _LoadBalancingStrategy.ValueType  # 6
    """p2c with least connections from metadata"""


LoadBalancingStrategy: LoadBalancingStrategy

class LoadBalancingStrategy(_LoadBalancingStrategy, metaclass=_LoadBalancingStrategyEnumTypeWrapper):
    """Deprecated and will be removed in next versions"""
    pass

wrr: LoadBalancingStrategy.ValueType  # 0
"""Weighted round robin"""

random: LoadBalancingStrategy.ValueType  # 1
"""Random"""

consthash: LoadBalancingStrategy.ValueType  # 2
"""Consistent hashing"""

p2c: LoadBalancingStrategy.ValueType  # 3
"""Power of 2 choices"""

p2clc: LoadBalancingStrategy.ValueType  # 4
"""p2c with least connections (default for p2c strategy)"""

p2crt: LoadBalancingStrategy.ValueType  # 5
"""p2c with response time load adviser"""

p2cmd: LoadBalancingStrategy.ValueType  # 6
"""p2c with least connections from metadata"""



_ListenMode: _ListenMode

class _ListenMode:
    ValueType = NewType('ValueType', int)
    V: TypeAlias = ValueType

_ListenModeEnumTypeWrapper: _ListenModeEnumTypeWrapper

class _ListenModeEnumTypeWrapper(EnumTypeWrapper[_ListenMode.ValueType], type):
    DESCRIPTOR: EnumDescriptor
    all: _ListenMode.ValueType  # 0
    """send upstream host from from all data centers"""

    auto: _ListenMode.ValueType  # 1
    """sends local upstream hosts if exits, or all otherwise"""

    local: _ListenMode.ValueType  # 2
    """send upstream hosts only from local DC"""


ListenMode: ListenMode

class ListenMode(_ListenMode, metaclass=_ListenModeEnumTypeWrapper):
    """Identifies mode in which clients listen for upstream host's updates"""
    pass

all: ListenMode.ValueType  # 0
"""send upstream host from from all data centers"""

auto: ListenMode.ValueType  # 1
"""sends local upstream hosts if exits, or all otherwise"""

local: ListenMode.ValueType  # 2
"""send upstream hosts only from local DC"""



_MSSqlNodeRole: _MSSqlNodeRole

class _MSSqlNodeRole:
    ValueType = NewType('ValueType', int)
    V: TypeAlias = ValueType

_MSSqlNodeRoleEnumTypeWrapper: _MSSqlNodeRoleEnumTypeWrapper

class _MSSqlNodeRoleEnumTypeWrapper(EnumTypeWrapper[_MSSqlNodeRole.ValueType], type):
    DESCRIPTOR: EnumDescriptor
    master: _MSSqlNodeRole.ValueType  # 0
    sync: _MSSqlNodeRole.ValueType  # 2

MSSqlNodeRole: MSSqlNodeRole

class MSSqlNodeRole(_MSSqlNodeRole, metaclass=_MSSqlNodeRoleEnumTypeWrapper):
    """MSSqlNodeRole defines types of mssql node role"""
    pass

master: MSSqlNodeRole.ValueType  # 0
sync: MSSqlNodeRole.ValueType  # 2


Locality: Locality

class Locality(Message):
    """Identifies location of where upstream hosts run."""
    DESCRIPTOR: Descriptor
    REGION_FIELD_NUMBER: int
    ZONE_FIELD_NUMBER: int
    SUB_ZONE_FIELD_NUMBER: int
    region: Text
    """Region this :ref:`zone <endpoints.v1.Locality.zone>` belongs to."""

    zone: Text
    """Defines the local service zone where upstream host is running."""

    sub_zone: Text
    """When used for locality of upstream hosts, this field further splits zone
    into smaller chunks of sub-zones so they can be load balanced
    independently.
    """

    def __init__(self,
        *,
        region: Text = ...,
        zone: Text = ...,
        sub_zone: Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: Literal["region",b"region","sub_zone",b"sub_zone","zone",b"zone"]) -> None: ...


SubsettingOptions: SubsettingOptions

class SubsettingOptions(Message):
    DESCRIPTOR: Descriptor
    class IDSettings(Message):
        DESCRIPTOR: Descriptor
        ID_FIELD_NUMBER: int
        TOTAL_ENDPOINTS_FIELD_NUMBER: int
        id: int
        total_endpoints: int
        def __init__(self,
            *,
            id: int = ...,
            total_endpoints: int = ...,
            ) -> None: ...
        def ClearField(self, field_name: Literal["id",b"id","total_endpoints",b"total_endpoints"]) -> None: ...

    DISABLED_FIELD_NUMBER: int
    CLIENT_IP_FIELD_NUMBER: int
    ID_SETTINGS_FIELD_NUMBER: int
    LOWER_BOUND_FIELD_NUMBER: int
    REPLICA_FACTOR_FIELD_NUMBER: int
    disabled: bool
    client_ip: Text
    @property
    def id_settings(self) -> SubsettingOptions.IDSettings: ...
    @property
    def lower_bound(self) -> UInt32Value: ...
    @property
    def replica_factor(self) -> UInt32Value: ...
    def __init__(self,
        *,
        disabled: bool = ...,
        client_ip: Text = ...,
        id_settings: Optional[SubsettingOptions.IDSettings] = ...,
        lower_bound: Optional[UInt32Value] = ...,
        replica_factor: Optional[UInt32Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["client_ip",b"client_ip","id_settings",b"id_settings","lower_bound",b"lower_bound","override",b"override","replica_factor",b"replica_factor"]) -> bool: ...
    def ClearField(self, field_name: Literal["client_ip",b"client_ip","disabled",b"disabled","id_settings",b"id_settings","lower_bound",b"lower_bound","override",b"override","replica_factor",b"replica_factor"]) -> None: ...
    def WhichOneof(self, oneof_group: Literal["override",b"override"]) -> Optional[Literal["client_ip","id_settings"]]: ...


SubsettingDebug: SubsettingDebug

class SubsettingDebug(Message):
    DESCRIPTOR: Descriptor
    VERSION_FIELD_NUMBER: int
    ORIGINAL_CLIENTS_LENGTH_FIELD_NUMBER: int
    ORIGINAL_BACKENDS_LENGTH_FIELD_NUMBER: int
    RESULT_BACKENDS_LENGTH_FIELD_NUMBER: int
    SUBSET_SIZE_FIELD_NUMBER: int
    CLIENT_ID_FIELD_NUMBER: int
    version: Text
    original_clients_length: int
    original_backends_length: int
    result_backends_length: int
    subset_size: int
    client_id: int
    def __init__(self,
        *,
        version: Text = ...,
        original_clients_length: int = ...,
        original_backends_length: int = ...,
        result_backends_length: int = ...,
        subset_size: int = ...,
        client_id: int = ...,
        ) -> None: ...
    def ClearField(self, field_name: Literal["client_id",b"client_id","original_backends_length",b"original_backends_length","original_clients_length",b"original_clients_length","result_backends_length",b"result_backends_length","subset_size",b"subset_size","version",b"version"]) -> None: ...


UpdateInfo: UpdateInfo

class UpdateInfo(Message):
    DESCRIPTOR: Descriptor
    APP_HASH_FIELD_NUMBER: int
    LOCAL_VERSION_ID_FIELD_NUMBER: int
    EVENT_TS_FIELD_NUMBER: int
    app_hash: int
    local_version_id: int
    @property
    def event_ts(self) -> Timestamp: ...
    def __init__(self,
        *,
        app_hash: int = ...,
        local_version_id: int = ...,
        event_ts: Optional[Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["event_ts",b"event_ts"]) -> bool: ...
    def ClearField(self, field_name: Literal["app_hash",b"app_hash","event_ts",b"event_ts","local_version_id",b"local_version_id"]) -> None: ...


GetEndpointsRequest: GetEndpointsRequest

class GetEndpointsRequest(Message):
    DESCRIPTOR: Descriptor
    SERVICE_FIELD_NUMBER: int
    MODE_FIELD_NUMBER: int
    LOCALITY_FIELD_NUMBER: int
    SUBSETTING_OPTIONS_FIELD_NUMBER: int
    service: Text
    """name of the service in the form <service>.<namespace>:<port> For example:

    - catalog-api.bx:grpc
    - pdp-api.bx:grpc
    - tarrifficator-api.geo:grpc
    """

    mode: ListenMode.ValueType
    @property
    def locality(self) -> Locality: ...
    @property
    def subsetting_options(self) -> SubsettingOptions: ...
    def __init__(self,
        *,
        service: Text = ...,
        mode: ListenMode.ValueType = ...,
        locality: Optional[Locality] = ...,
        subsetting_options: Optional[SubsettingOptions] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["locality",b"locality","subsetting_options",b"subsetting_options"]) -> bool: ...
    def ClearField(self, field_name: Literal["locality",b"locality","mode",b"mode","service",b"service","subsetting_options",b"subsetting_options"]) -> None: ...


WatchEndpointsRequest: WatchEndpointsRequest

class WatchEndpointsRequest(Message):
    DESCRIPTOR: Descriptor
    SERVICE_FIELD_NUMBER: int
    MODE_FIELD_NUMBER: int
    LOCALITY_FIELD_NUMBER: int
    SUBSETTING_OPTIONS_FIELD_NUMBER: int
    service: Text
    """name of the service in the form <service>.<namespace>:<port> For example:

    - catalog-api.bx:grpc
    - pdp-api.bx:grpc
    - tarrifficator-api.geo:grpc
    """

    mode: ListenMode.ValueType
    @property
    def locality(self) -> Locality: ...
    @property
    def subsetting_options(self) -> SubsettingOptions: ...
    def __init__(self,
        *,
        service: Text = ...,
        mode: ListenMode.ValueType = ...,
        locality: Optional[Locality] = ...,
        subsetting_options: Optional[SubsettingOptions] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["locality",b"locality","subsetting_options",b"subsetting_options"]) -> bool: ...
    def ClearField(self, field_name: Literal["locality",b"locality","mode",b"mode","service",b"service","subsetting_options",b"subsetting_options"]) -> None: ...


GetEndpointsResponse: GetEndpointsResponse

class GetEndpointsResponse(Message):
    DESCRIPTOR: Descriptor
    ENDPOINTS_FIELD_NUMBER: int
    SERVICE_CONFIG_FIELD_NUMBER: int
    SUBSETTING_DEBUG_FIELD_NUMBER: int
    @property
    def endpoints(self) -> RepeatedCompositeFieldContainer[Endpoint]:
        """full list of currently active endpoints."""
        pass
    service_config: Text
    """service configuration as described here:
    https://github.com/grpc/grpc/blob/master/doc/service_config.md
    """

    @property
    def subsetting_debug(self) -> RepeatedCompositeFieldContainer[SubsettingDebug]: ...
    def __init__(self,
        *,
        endpoints: Optional[Iterable[Endpoint]] = ...,
        service_config: Text = ...,
        subsetting_debug: Optional[Iterable[SubsettingDebug]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: Literal["endpoints",b"endpoints","service_config",b"service_config","subsetting_debug",b"subsetting_debug"]) -> None: ...


WatchEndpointsResponse: WatchEndpointsResponse

class WatchEndpointsResponse(Message):
    DESCRIPTOR: Descriptor
    ENDPOINTS_FIELD_NUMBER: int
    SERVICE_CONFIG_FIELD_NUMBER: int
    SUBSETTING_DEBUG_FIELD_NUMBER: int
    UPDATE_INFO_FIELD_NUMBER: int
    @property
    def endpoints(self) -> RepeatedCompositeFieldContainer[Endpoint]:
        """full list of currently active endpoints."""
        pass
    service_config: Text
    """service configuration as described here:
    https://github.com/grpc/grpc/blob/master/doc/service_config.md
    """

    @property
    def subsetting_debug(self) -> RepeatedCompositeFieldContainer[SubsettingDebug]: ...
    @property
    def update_info(self) -> UpdateInfo: ...
    def __init__(self,
        *,
        endpoints: Optional[Iterable[Endpoint]] = ...,
        service_config: Text = ...,
        subsetting_debug: Optional[Iterable[SubsettingDebug]] = ...,
        update_info: Optional[UpdateInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["update_info",b"update_info"]) -> bool: ...
    def ClearField(self, field_name: Literal["endpoints",b"endpoints","service_config",b"service_config","subsetting_debug",b"subsetting_debug","update_info",b"update_info"]) -> None: ...


Endpoint: Endpoint

class Endpoint(Message):
    """Endpoint defines data that will be mapped to gRPC's resolver.Address:
    https://pkg.go.dev/google.golang.org/grpc@v1.33.2/resolver?tab=doc#Address
    """
    DESCRIPTOR: Descriptor
    class Attributes(Message):
        DESCRIPTOR: Descriptor
        IS_DEFAULT_VERSION_FIELD_NUMBER: int
        WEIGHT_FIELD_NUMBER: int
        VERSION_FIELD_NUMBER: int
        is_default_version: bool
        weight: int
        version: Text
        def __init__(self,
            *,
            is_default_version: bool = ...,
            weight: int = ...,
            version: Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: Literal["is_default_version",b"is_default_version","version",b"version","weight",b"weight"]) -> None: ...

    class AttributesEntry(Message):
        DESCRIPTOR: Descriptor
        KEY_FIELD_NUMBER: int
        VALUE_FIELD_NUMBER: int
        key: Text
        value: Text
        def __init__(self,
            *,
            key: Text = ...,
            value: Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: Literal["key",b"key","value",b"value"]) -> None: ...

    ADDRESS_FIELD_NUMBER: int
    NAME_FIELD_NUMBER: int
    ATTRIBUTES_FIELD_NUMBER: int
    LOCALITY_FIELD_NUMBER: int
    ATTRS_FIELD_NUMBER: int
    address: Text
    """endpoint address in host:port form."""

    name: Text
    """pod name will be used as endpoint's name."""

    @property
    def attributes(self) -> ScalarMap[Text, Text]:
        """additional attributes. Warden sets following attributes for every endpoint:

        1. version. It's value of `app.kubernetes.io/version` pod's label.

        2. isDefaultRoute. If true, then this endpoints is used in default route.
        more details: https://confluence.ozon.ru/display/ITDOC/Common+pipeline+0.0.5+jobs

        3. weight. Defines weight of this endpoint for traffic balancing. More the weight then more
        requests has to be sent to this endpoint.

        Additionally any other attributes can be set.
        """
        pass
    @property
    def locality(self) -> Locality:
        """Locality is which this endpoint runs"""
        pass
    @property
    def attrs(self) -> Endpoint.Attributes: ...
    def __init__(self,
        *,
        address: Text = ...,
        name: Text = ...,
        attributes: Optional[Mapping[Text, Text]] = ...,
        locality: Optional[Locality] = ...,
        attrs: Optional[Endpoint.Attributes] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["attrs",b"attrs","locality",b"locality"]) -> bool: ...
    def ClearField(self, field_name: Literal["address",b"address","attributes",b"attributes","attrs",b"attrs","locality",b"locality","name",b"name"]) -> None: ...


MSSqlEndpoint: MSSqlEndpoint

class MSSqlEndpoint(Message):
    """MSSqlEndpoint defines information about mssql node"""
    DESCRIPTOR: Descriptor
    ADDRESS_FIELD_NUMBER: int
    NODE_ROLE_FIELD_NUMBER: int
    address: Text
    """Address is the host and port to connect to the node"""

    node_role: MSSqlNodeRole.ValueType
    """The role of the node"""

    def __init__(self,
        *,
        address: Text = ...,
        node_role: MSSqlNodeRole.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: Literal["address",b"address","node_role",b"node_role"]) -> None: ...


GetMSSQLEndpointsRequest: GetMSSQLEndpointsRequest

class GetMSSQLEndpointsRequest(Message):
    """GetMSSQLEndpointsRequest defines the request for getting information about mssql nodes in the cluster"""
    DESCRIPTOR: Descriptor
    CLUSTER_FIELD_NUMBER: int
    MODE_FIELD_NUMBER: int
    LOCALITY_FIELD_NUMBER: int
    cluster: Text
    """name of the cluster in the form <cluster>.mssql:<port> For example:

    - bodb.mssql:direct
    - findb.mssql:direct
    """

    mode: ListenMode.ValueType
    @property
    def locality(self) -> Locality: ...
    def __init__(self,
        *,
        cluster: Text = ...,
        mode: ListenMode.ValueType = ...,
        locality: Optional[Locality] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["locality",b"locality"]) -> bool: ...
    def ClearField(self, field_name: Literal["cluster",b"cluster","locality",b"locality","mode",b"mode"]) -> None: ...


GetMSSQLEndpointsResponse: GetMSSQLEndpointsResponse

class GetMSSQLEndpointsResponse(Message):
    """GetMSSQLEndpointsResponse defines the response to the request for mssql nodes in the cluster"""
    DESCRIPTOR: Descriptor
    ENDPOINTS_FIELD_NUMBER: int
    @property
    def endpoints(self) -> RepeatedCompositeFieldContainer[MSSqlEndpoint]:
        """full list of currently active endpoints."""
        pass
    def __init__(self,
        *,
        endpoints: Optional[Iterable[MSSqlEndpoint]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: Literal["endpoints",b"endpoints"]) -> None: ...


WatchMSSQLEndpointsRequest: WatchMSSQLEndpointsRequest

class WatchMSSQLEndpointsRequest(Message):
    """WatchMSSQLEndpointsRequest defines the request for getting information about mssql nodes in the cluster"""
    DESCRIPTOR: Descriptor
    CLUSTER_FIELD_NUMBER: int
    MODE_FIELD_NUMBER: int
    LOCALITY_FIELD_NUMBER: int
    cluster: Text
    """name of the cluster in the form <cluster>.mssql:<port> For example:

    - bodb.mssql:direct
    - findb.mssql:direct
    """

    mode: ListenMode.ValueType
    @property
    def locality(self) -> Locality: ...
    def __init__(self,
        *,
        cluster: Text = ...,
        mode: ListenMode.ValueType = ...,
        locality: Optional[Locality] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["locality",b"locality"]) -> bool: ...
    def ClearField(self, field_name: Literal["cluster",b"cluster","locality",b"locality","mode",b"mode"]) -> None: ...


WatchMSSQLEndpointsResponse: WatchMSSQLEndpointsResponse

class WatchMSSQLEndpointsResponse(Message):
    """WatchMSSQLEndpointsResponse defines the response to the request for mssql nodes in the cluster"""
    DESCRIPTOR: Descriptor
    ENDPOINTS_FIELD_NUMBER: int
    @property
    def endpoints(self) -> RepeatedCompositeFieldContainer[MSSqlEndpoint]:
        """full list of currently active endpoints."""
        pass
    def __init__(self,
        *,
        endpoints: Optional[Iterable[MSSqlEndpoint]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: Literal["endpoints",b"endpoints"]) -> None: ...
