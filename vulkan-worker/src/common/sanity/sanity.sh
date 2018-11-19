#!/bin/bash

# Copyright 2018 The GraphicsFuzz Project Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -e
set -x

glslangValidator -V -o sanity.vert.spv sanity.vert
(
  echo "// This file was generated by: xxd -i sanity.vert.spv"
  xxd -i sanity.vert.spv
) > sanity_vert.inc

glslangValidator -V -o sanity.frag.spv sanity.frag
(
  echo "// This file was generated by: xxd -i sanity.frag.spv"
  xxd -i sanity.frag.spv
) > sanity_frag.inc