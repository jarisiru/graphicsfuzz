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


class Recipe(google___protobuf___message___Message):

    @property
    def command(self) -> RecipeCommand: ...

    @property
    def glsl_shader_job_to_spirv_shader_job(self) -> RecipeGlslShaderJobToSpirvShaderJob: ...

    @property
    def spirv_shader_job_to_spirv_shader_job_opt(self) -> RecipeSpirvShaderJobToSpirvShaderJobOpt: ...

    @property
    def glsl_shader_job_add_red_pixels(self) -> RecipeGlslShaderJobAddRedPixels: ...

    @property
    def spirv_asm_shader_job_to_amber_script(self) -> RecipeSpirvAsmShaderJobToAmberScript: ...

    @property
    def spirv_shader_job_to_spirv_asm_shader_job(self) -> RecipeSpirvShaderJobToSpirvAsmShaderJob: ...

    def __init__(self,
        command : typing___Optional[RecipeCommand] = None,
        glsl_shader_job_to_spirv_shader_job : typing___Optional[RecipeGlslShaderJobToSpirvShaderJob] = None,
        spirv_shader_job_to_spirv_shader_job_opt : typing___Optional[RecipeSpirvShaderJobToSpirvShaderJobOpt] = None,
        glsl_shader_job_add_red_pixels : typing___Optional[RecipeGlslShaderJobAddRedPixels] = None,
        spirv_asm_shader_job_to_amber_script : typing___Optional[RecipeSpirvAsmShaderJobToAmberScript] = None,
        spirv_shader_job_to_spirv_asm_shader_job : typing___Optional[RecipeSpirvShaderJobToSpirvAsmShaderJob] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Recipe: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"command",u"glsl_shader_job_add_red_pixels",u"glsl_shader_job_to_spirv_shader_job",u"recipe",u"spirv_asm_shader_job_to_amber_script",u"spirv_shader_job_to_spirv_asm_shader_job",u"spirv_shader_job_to_spirv_shader_job_opt"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"command",u"glsl_shader_job_add_red_pixels",u"glsl_shader_job_to_spirv_shader_job",u"recipe",u"spirv_asm_shader_job_to_amber_script",u"spirv_shader_job_to_spirv_asm_shader_job",u"spirv_shader_job_to_spirv_shader_job_opt"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"command",b"command",u"glsl_shader_job_add_red_pixels",b"glsl_shader_job_add_red_pixels",u"glsl_shader_job_to_spirv_shader_job",b"glsl_shader_job_to_spirv_shader_job",u"recipe",b"recipe",u"spirv_asm_shader_job_to_amber_script",b"spirv_asm_shader_job_to_amber_script",u"spirv_shader_job_to_spirv_asm_shader_job",b"spirv_shader_job_to_spirv_asm_shader_job",u"spirv_shader_job_to_spirv_shader_job_opt",b"spirv_shader_job_to_spirv_shader_job_opt"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"command",b"glsl_shader_job_add_red_pixels",b"glsl_shader_job_to_spirv_shader_job",b"recipe",b"spirv_asm_shader_job_to_amber_script",b"spirv_shader_job_to_spirv_asm_shader_job",b"spirv_shader_job_to_spirv_shader_job_opt"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"recipe",b"recipe"]) -> typing_extensions___Literal["command","glsl_shader_job_to_spirv_shader_job","spirv_shader_job_to_spirv_shader_job_opt","glsl_shader_job_add_red_pixels","spirv_asm_shader_job_to_amber_script","spirv_shader_job_to_spirv_asm_shader_job"]: ...

class RecipeCommand(google___protobuf___message___Message):
    command = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        command : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RecipeCommand: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"command"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"command"]) -> None: ...

class RecipeGlslShaderJobToSpirvShaderJob(google___protobuf___message___Message):
    glsl_shader_job_artifact = ... # type: typing___Text
    glslang_validator_artifact = ... # type: typing___Text

    def __init__(self,
        glsl_shader_job_artifact : typing___Optional[typing___Text] = None,
        glslang_validator_artifact : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RecipeGlslShaderJobToSpirvShaderJob: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"glsl_shader_job_artifact",u"glslang_validator_artifact"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"glsl_shader_job_artifact",b"glslang_validator_artifact"]) -> None: ...

class RecipeSpirvShaderJobToSpirvShaderJobOpt(google___protobuf___message___Message):
    spirv_shader_job_artifact = ... # type: typing___Text
    spirv_opt_args = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    spirv_opt_artifact = ... # type: typing___Text

    def __init__(self,
        spirv_shader_job_artifact : typing___Optional[typing___Text] = None,
        spirv_opt_args : typing___Optional[typing___Iterable[typing___Text]] = None,
        spirv_opt_artifact : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RecipeSpirvShaderJobToSpirvShaderJobOpt: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"spirv_opt_args",u"spirv_opt_artifact",u"spirv_shader_job_artifact"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"spirv_opt_args",b"spirv_opt_artifact",b"spirv_shader_job_artifact"]) -> None: ...

class RecipeGlslShaderJobAddRedPixels(google___protobuf___message___Message):
    glsl_shader_job_artifact = ... # type: typing___Text
    graphics_fuzz_artifact = ... # type: typing___Text

    def __init__(self,
        glsl_shader_job_artifact : typing___Optional[typing___Text] = None,
        graphics_fuzz_artifact : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RecipeGlslShaderJobAddRedPixels: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"glsl_shader_job_artifact",u"graphics_fuzz_artifact"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"glsl_shader_job_artifact",b"graphics_fuzz_artifact"]) -> None: ...

class RecipeSpirvShaderJobToSpirvAsmShaderJob(google___protobuf___message___Message):
    spirv_shader_job_artifact = ... # type: typing___Text
    spirv_dis_artifact = ... # type: typing___Text

    def __init__(self,
        spirv_shader_job_artifact : typing___Optional[typing___Text] = None,
        spirv_dis_artifact : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RecipeSpirvShaderJobToSpirvAsmShaderJob: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"spirv_dis_artifact",u"spirv_shader_job_artifact"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"spirv_dis_artifact",b"spirv_shader_job_artifact"]) -> None: ...

class RecipeSpirvAsmShaderJobToAmberScript(google___protobuf___message___Message):
    spirv_asm_shader_job_artifact = ... # type: typing___Text
    make_self_contained_test = ... # type: bool
    amber_script_output_file = ... # type: typing___Text
    copyright_header_text_artifact = ... # type: typing___Text
    add_generated_comment = ... # type: bool
    add_graphics_fuzz_comment = ... # type: bool
    comment_text_artifact = ... # type: typing___Text
    add_glsl_source_as_comment = ... # type: bool
    default_fence_timeout = ... # type: bool

    def __init__(self,
        spirv_asm_shader_job_artifact : typing___Optional[typing___Text] = None,
        make_self_contained_test : typing___Optional[bool] = None,
        amber_script_output_file : typing___Optional[typing___Text] = None,
        copyright_header_text_artifact : typing___Optional[typing___Text] = None,
        add_generated_comment : typing___Optional[bool] = None,
        add_graphics_fuzz_comment : typing___Optional[bool] = None,
        comment_text_artifact : typing___Optional[typing___Text] = None,
        add_glsl_source_as_comment : typing___Optional[bool] = None,
        default_fence_timeout : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RecipeSpirvAsmShaderJobToAmberScript: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"add_generated_comment",u"add_glsl_source_as_comment",u"add_graphics_fuzz_comment",u"amber_script_output_file",u"comment_text_artifact",u"copyright_header_text_artifact",u"default_fence_timeout",u"make_self_contained_test",u"spirv_asm_shader_job_artifact"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"add_generated_comment",b"add_glsl_source_as_comment",b"add_graphics_fuzz_comment",b"amber_script_output_file",b"comment_text_artifact",b"copyright_header_text_artifact",b"default_fence_timeout",b"make_self_contained_test",b"spirv_asm_shader_job_artifact"]) -> None: ...
