# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from gfauto.common_pb2 import (
    Binary as gfauto___common_pb2___Binary,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class DeviceList(google___protobuf___message___Message):
    active_device_names = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def devices(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Device]: ...

    def __init__(self,
        active_device_names : typing___Optional[typing___Iterable[typing___Text]] = None,
        devices : typing___Optional[typing___Iterable[Device]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeviceList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"active_device_names",u"devices"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"active_device_names",b"devices"]) -> None: ...

class Device(google___protobuf___message___Message):
    name = ... # type: typing___Text

    @property
    def preprocess(self) -> DevicePreprocess: ...

    @property
    def swift_shader(self) -> DeviceSwiftShader: ...

    @property
    def host(self) -> DeviceHost: ...

    @property
    def android(self) -> DeviceAndroid: ...

    @property
    def binaries(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[gfauto___common_pb2___Binary]: ...

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        preprocess : typing___Optional[DevicePreprocess] = None,
        swift_shader : typing___Optional[DeviceSwiftShader] = None,
        host : typing___Optional[DeviceHost] = None,
        android : typing___Optional[DeviceAndroid] = None,
        binaries : typing___Optional[typing___Iterable[gfauto___common_pb2___Binary]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Device: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"android",u"device",u"host",u"preprocess",u"swift_shader"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"android",u"binaries",u"device",u"host",u"name",u"preprocess",u"swift_shader"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"android",b"android",u"device",b"device",u"host",b"host",u"preprocess",b"preprocess",u"swift_shader",b"swift_shader"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"android",b"binaries",b"device",b"host",b"name",b"preprocess",b"swift_shader"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"device",b"device"]) -> typing_extensions___Literal["preprocess","swift_shader","host","android"]: ...

class DeviceSwiftShader(google___protobuf___message___Message):

    @property
    def swift_shader_binary(self) -> gfauto___common_pb2___Binary: ...

    def __init__(self,
        swift_shader_binary : typing___Optional[gfauto___common_pb2___Binary] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeviceSwiftShader: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"swift_shader_binary"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"swift_shader_binary"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"swift_shader_binary",b"swift_shader_binary"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"swift_shader_binary"]) -> None: ...

class DevicePreprocess(google___protobuf___message___Message):

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DevicePreprocess: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class DeviceHost(google___protobuf___message___Message):

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeviceHost: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class DeviceAndroid(google___protobuf___message___Message):
    serial = ... # type: typing___Text
    model = ... # type: typing___Text

    def __init__(self,
        serial : typing___Optional[typing___Text] = None,
        model : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeviceAndroid: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"model",u"serial"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"model",b"serial"]) -> None: ...
