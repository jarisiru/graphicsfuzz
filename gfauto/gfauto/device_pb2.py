# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gfauto/device.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gfauto import common_pb2 as gfauto_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gfauto/device.proto',
  package='gfauto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13gfauto/device.proto\x12\x06gfauto\x1a\x13gfauto/common.proto\"J\n\nDeviceList\x12\x1b\n\x13\x61\x63tive_device_names\x18\x01 \x03(\t\x12\x1f\n\x07\x64\x65vices\x18\x02 \x03(\x0b\x32\x0e.gfauto.Device\"\xf3\x01\n\x06\x44\x65vice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\npreprocess\x18\x02 \x01(\x0b\x32\x18.gfauto.DevicePreprocessH\x00\x12\x31\n\x0cswift_shader\x18\x03 \x01(\x0b\x32\x19.gfauto.DeviceSwiftShaderH\x00\x12\"\n\x04host\x18\x04 \x01(\x0b\x32\x12.gfauto.DeviceHostH\x00\x12(\n\x07\x61ndroid\x18\x05 \x01(\x0b\x32\x15.gfauto.DeviceAndroidH\x00\x12 \n\x08\x62inaries\x18\x06 \x03(\x0b\x32\x0e.gfauto.BinaryB\x08\n\x06\x64\x65vice\"@\n\x11\x44\x65viceSwiftShader\x12+\n\x13swift_shader_binary\x18\x01 \x01(\x0b\x32\x0e.gfauto.Binary\"\x12\n\x10\x44\x65vicePreprocess\"\x0c\n\nDeviceHost\".\n\rDeviceAndroid\x12\x0e\n\x06serial\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\tb\x06proto3')
  ,
  dependencies=[gfauto_dot_common__pb2.DESCRIPTOR,])




_DEVICELIST = _descriptor.Descriptor(
  name='DeviceList',
  full_name='gfauto.DeviceList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='active_device_names', full_name='gfauto.DeviceList.active_device_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='devices', full_name='gfauto.DeviceList.devices', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=126,
)


_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='gfauto.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gfauto.Device.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preprocess', full_name='gfauto.Device.preprocess', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='swift_shader', full_name='gfauto.Device.swift_shader', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='gfauto.Device.host', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='android', full_name='gfauto.Device.android', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binaries', full_name='gfauto.Device.binaries', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='device', full_name='gfauto.Device.device',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=129,
  serialized_end=372,
)


_DEVICESWIFTSHADER = _descriptor.Descriptor(
  name='DeviceSwiftShader',
  full_name='gfauto.DeviceSwiftShader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='swift_shader_binary', full_name='gfauto.DeviceSwiftShader.swift_shader_binary', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=438,
)


_DEVICEPREPROCESS = _descriptor.Descriptor(
  name='DevicePreprocess',
  full_name='gfauto.DevicePreprocess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=458,
)


_DEVICEHOST = _descriptor.Descriptor(
  name='DeviceHost',
  full_name='gfauto.DeviceHost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=472,
)


_DEVICEANDROID = _descriptor.Descriptor(
  name='DeviceAndroid',
  full_name='gfauto.DeviceAndroid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serial', full_name='gfauto.DeviceAndroid.serial', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='gfauto.DeviceAndroid.model', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=474,
  serialized_end=520,
)

_DEVICELIST.fields_by_name['devices'].message_type = _DEVICE
_DEVICE.fields_by_name['preprocess'].message_type = _DEVICEPREPROCESS
_DEVICE.fields_by_name['swift_shader'].message_type = _DEVICESWIFTSHADER
_DEVICE.fields_by_name['host'].message_type = _DEVICEHOST
_DEVICE.fields_by_name['android'].message_type = _DEVICEANDROID
_DEVICE.fields_by_name['binaries'].message_type = gfauto_dot_common__pb2._BINARY
_DEVICE.oneofs_by_name['device'].fields.append(
  _DEVICE.fields_by_name['preprocess'])
_DEVICE.fields_by_name['preprocess'].containing_oneof = _DEVICE.oneofs_by_name['device']
_DEVICE.oneofs_by_name['device'].fields.append(
  _DEVICE.fields_by_name['swift_shader'])
_DEVICE.fields_by_name['swift_shader'].containing_oneof = _DEVICE.oneofs_by_name['device']
_DEVICE.oneofs_by_name['device'].fields.append(
  _DEVICE.fields_by_name['host'])
_DEVICE.fields_by_name['host'].containing_oneof = _DEVICE.oneofs_by_name['device']
_DEVICE.oneofs_by_name['device'].fields.append(
  _DEVICE.fields_by_name['android'])
_DEVICE.fields_by_name['android'].containing_oneof = _DEVICE.oneofs_by_name['device']
_DEVICESWIFTSHADER.fields_by_name['swift_shader_binary'].message_type = gfauto_dot_common__pb2._BINARY
DESCRIPTOR.message_types_by_name['DeviceList'] = _DEVICELIST
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['DeviceSwiftShader'] = _DEVICESWIFTSHADER
DESCRIPTOR.message_types_by_name['DevicePreprocess'] = _DEVICEPREPROCESS
DESCRIPTOR.message_types_by_name['DeviceHost'] = _DEVICEHOST
DESCRIPTOR.message_types_by_name['DeviceAndroid'] = _DEVICEANDROID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceList = _reflection.GeneratedProtocolMessageType('DeviceList', (_message.Message,), dict(
  DESCRIPTOR = _DEVICELIST,
  __module__ = 'gfauto.device_pb2'
  # @@protoc_insertion_point(class_scope:gfauto.DeviceList)
  ))
_sym_db.RegisterMessage(DeviceList)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), dict(
  DESCRIPTOR = _DEVICE,
  __module__ = 'gfauto.device_pb2'
  # @@protoc_insertion_point(class_scope:gfauto.Device)
  ))
_sym_db.RegisterMessage(Device)

DeviceSwiftShader = _reflection.GeneratedProtocolMessageType('DeviceSwiftShader', (_message.Message,), dict(
  DESCRIPTOR = _DEVICESWIFTSHADER,
  __module__ = 'gfauto.device_pb2'
  # @@protoc_insertion_point(class_scope:gfauto.DeviceSwiftShader)
  ))
_sym_db.RegisterMessage(DeviceSwiftShader)

DevicePreprocess = _reflection.GeneratedProtocolMessageType('DevicePreprocess', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEPREPROCESS,
  __module__ = 'gfauto.device_pb2'
  # @@protoc_insertion_point(class_scope:gfauto.DevicePreprocess)
  ))
_sym_db.RegisterMessage(DevicePreprocess)

DeviceHost = _reflection.GeneratedProtocolMessageType('DeviceHost', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEHOST,
  __module__ = 'gfauto.device_pb2'
  # @@protoc_insertion_point(class_scope:gfauto.DeviceHost)
  ))
_sym_db.RegisterMessage(DeviceHost)

DeviceAndroid = _reflection.GeneratedProtocolMessageType('DeviceAndroid', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEANDROID,
  __module__ = 'gfauto.device_pb2'
  # @@protoc_insertion_point(class_scope:gfauto.DeviceAndroid)
  ))
_sym_db.RegisterMessage(DeviceAndroid)


# @@protoc_insertion_point(module_scope)
