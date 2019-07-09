# -*- coding: utf-8 -*-

# Copyright 2019 The GraphicsFuzz Project Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pathlib
from pathlib import Path
from typing import List, Optional

from gfauto import subprocess_util, util


def run_generate(
    graphicsfuzz_tool_path: Path,
    reference_shader_json: pathlib.Path,
    donors_path: pathlib.Path,
    output_shader_json: pathlib.Path,
    seed: Optional[str] = None,
    other_args: Optional[List[str]] = None,
) -> pathlib.Path:
    util.file_mkdirs_parent(output_shader_json)
    cmd = [
        str(graphicsfuzz_tool_path),
        "com.graphicsfuzz.generator.tool.Generate",
        str(reference_shader_json),
        str(donors_path),
        "100",  # TODO(215): remove once #215 is closed again.
        str(output_shader_json),
        "--generate-uniform-bindings",
        "--max-uniforms",
        "10",
    ]

    if seed:
        cmd.append(f"--seed={seed}")

    if other_args:
        cmd.extend(other_args)

    subprocess_util.run(cmd)

    return output_shader_json
