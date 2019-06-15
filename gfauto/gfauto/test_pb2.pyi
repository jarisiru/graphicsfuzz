# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
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


class Test(google___protobuf___message___Message):

    @property
    def glsl(self) -> TestGlsl: ...

    def __init__(self,
        glsl : typing___Optional[TestGlsl] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Test: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"glsl",u"test"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"glsl",u"test"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"glsl",b"glsl",u"test",b"test"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"glsl",b"test"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"test",b"test"]) -> typing_extensions___Literal["glsl"]: ...

class TestGlsl(google___protobuf___message___Message):
    glslang_version_hash = ... # type: typing___Text
    spirv_opt_version_hash = ... # type: typing___Text
    spirv_opt_args = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        glslang_version_hash : typing___Optional[typing___Text] = None,
        spirv_opt_version_hash : typing___Optional[typing___Text] = None,
        spirv_opt_args : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> TestGlsl: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"glslang_version_hash",u"spirv_opt_args",u"spirv_opt_version_hash"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"glslang_version_hash",b"spirv_opt_args",b"spirv_opt_version_hash"]) -> None: ...