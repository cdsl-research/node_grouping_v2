# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='node.proto',
  package='node',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nnode.proto\x12\x04node\"i\n\rAddRequestDef\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x11\n\tsender_ip\x18\x03 \x01(\t\x12\x11\n\tboot_time\x18\x04 \x01(\x02\x12\x12\n\ntime_stamp\x18\x05 \x01(\x02\"W\n\x0e\x41\x64\x64ResponseDef\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1d\n\tnode_list\x18\x02 \x03(\x0b\x32\n.node.Node\x12\x12\n\ntime_stamp\x18\x03 \x01(\x02\"W\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x11\n\tboot_time\x18\x03 \x01(\x02\x12\x10\n\x08group_id\x18\x04 \x01(\x04\x12\x12\n\nis_primary\x18\x05 \x01(\x08\x32O\n\x11\x41\x64\x64RequestService\x12:\n\x0b\x61\x64\x64_request\x12\x13.node.AddRequestDef\x1a\x14.node.AddResponseDef\"\x00\x62\x06proto3'
)




_ADDREQUESTDEF = _descriptor.Descriptor(
  name='AddRequestDef',
  full_name='node.AddRequestDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='node.AddRequestDef.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='node.AddRequestDef.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender_ip', full_name='node.AddRequestDef.sender_ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='boot_time', full_name='node.AddRequestDef.boot_time', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='node.AddRequestDef.time_stamp', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=20,
  serialized_end=125,
)


_ADDRESPONSEDEF = _descriptor.Descriptor(
  name='AddResponseDef',
  full_name='node.AddResponseDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='node.AddResponseDef.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_list', full_name='node.AddResponseDef.node_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='node.AddResponseDef.time_stamp', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=127,
  serialized_end=214,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='node.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='node.Node.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='node.Node.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='boot_time', full_name='node.Node.boot_time', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='node.Node.group_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_primary', full_name='node.Node.is_primary', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=216,
  serialized_end=303,
)

_ADDRESPONSEDEF.fields_by_name['node_list'].message_type = _NODE
DESCRIPTOR.message_types_by_name['AddRequestDef'] = _ADDREQUESTDEF
DESCRIPTOR.message_types_by_name['AddResponseDef'] = _ADDRESPONSEDEF
DESCRIPTOR.message_types_by_name['Node'] = _NODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddRequestDef = _reflection.GeneratedProtocolMessageType('AddRequestDef', (_message.Message,), {
  'DESCRIPTOR' : _ADDREQUESTDEF,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:node.AddRequestDef)
  })
_sym_db.RegisterMessage(AddRequestDef)

AddResponseDef = _reflection.GeneratedProtocolMessageType('AddResponseDef', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESPONSEDEF,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:node.AddResponseDef)
  })
_sym_db.RegisterMessage(AddResponseDef)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:node.Node)
  })
_sym_db.RegisterMessage(Node)



_ADDREQUESTSERVICE = _descriptor.ServiceDescriptor(
  name='AddRequestService',
  full_name='node.AddRequestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=305,
  serialized_end=384,
  methods=[
  _descriptor.MethodDescriptor(
    name='add_request',
    full_name='node.AddRequestService.add_request',
    index=0,
    containing_service=None,
    input_type=_ADDREQUESTDEF,
    output_type=_ADDRESPONSEDEF,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADDREQUESTSERVICE)

DESCRIPTOR.services_by_name['AddRequestService'] = _ADDREQUESTSERVICE

# @@protoc_insertion_point(module_scope)
