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
  serialized_pb=b'\n\nnode.proto\x12\x04node\"i\n\rAddRequestDef\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x11\n\tsender_ip\x18\x03 \x01(\t\x12\x11\n\tboot_time\x18\x04 \x01(\x01\x12\x12\n\ntime_stamp\x18\x05 \x01(\x01\"W\n\x0e\x41\x64\x64ResponseDef\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1d\n\tnode_list\x18\x02 \x03(\x0b\x32\n.node.Node\x12\x12\n\ntime_stamp\x18\x03 \x01(\x01\"\x8f\x01\n\x12\x44iffNodeRequestDef\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x0f\n\x07node_id\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x11\n\tboot_time\x18\x05 \x01(\x01\x12\x11\n\tsender_ip\x18\x06 \x01(\t\x12\x12\n\ntime_stamp\x18\x07 \x01(\x01\"M\n\x13\x44iffNodeResponseDef\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x12\n\ntime_stamp\x18\x03 \x01(\x01\"M\n\x13HeartBeatRequestDef\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x12\n\ntime_stamp\x18\x03 \x01(\x01\"N\n\x14HeartBeatResponseDef\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x12\n\ntime_stamp\x18\x03 \x01(\x01\"a\n\x1aRequestHeartBeatRequestDef\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1b\n\x13\x64\x65stination_node_id\x18\x02 \x01(\t\x12\x12\n\ntime_stamp\x18\x03 \x01(\x01\"U\n\x1bRequestHeartBeatResponseDef\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x12\n\ntime_stamp\x18\x03 \x01(\x01\"?\n\x15NodesStatusRequestDef\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x12\n\ntime_stamp\x18\x02 \x01(\x01\"_\n\x16NodesStatusResponseDef\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1d\n\tnode_list\x18\x02 \x03(\x0b\x32\n.node.Node\x12\x12\n\ntime_stamp\x18\x03 \x01(\x01\"V\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x11\n\tboot_time\x18\x03 \x01(\x01\x12\x10\n\x08group_id\x18\x04 \x01(\x04\x12\x11\n\tis_leader\x18\x05 \x01(\x08\x32\x9c\x03\n\x0eRequestService\x12:\n\x0b\x61\x64\x64_request\x12\x13.node.AddRequestDef\x1a\x14.node.AddResponseDef\"\x00\x12G\n\x0eupdate_request\x12\x18.node.DiffNodeRequestDef\x1a\x19.node.DiffNodeResponseDef\"\x00\x12L\n\x11heartbeat_request\x12\x19.node.HeartBeatRequestDef\x1a\x1a.node.HeartBeatResponseDef\"\x00\x12\x62\n\x19request_heartbeat_request\x12 .node.RequestHeartBeatRequestDef\x1a!.node.RequestHeartBeatResponseDef\"\x00\x12S\n\x14nodes_status_request\x12\x1b.node.NodesStatusRequestDef\x1a\x1c.node.NodesStatusResponseDef\"\x00\x62\x06proto3'
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
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='node.AddRequestDef.time_stamp', index=4,
      number=5, type=1, cpp_type=5, label=1,
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
      number=3, type=1, cpp_type=5, label=1,
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


_DIFFNODEREQUESTDEF = _descriptor.Descriptor(
  name='DiffNodeRequestDef',
  full_name='node.DiffNodeRequestDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='node.DiffNodeRequestDef.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='method', full_name='node.DiffNodeRequestDef.method', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='node.DiffNodeRequestDef.node_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='node.DiffNodeRequestDef.ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='boot_time', full_name='node.DiffNodeRequestDef.boot_time', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender_ip', full_name='node.DiffNodeRequestDef.sender_ip', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='node.DiffNodeRequestDef.time_stamp', index=6,
      number=7, type=1, cpp_type=5, label=1,
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
  serialized_start=217,
  serialized_end=360,
)


_DIFFNODERESPONSEDEF = _descriptor.Descriptor(
  name='DiffNodeResponseDef',
  full_name='node.DiffNodeResponseDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='node.DiffNodeResponseDef.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='node.DiffNodeResponseDef.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='node.DiffNodeResponseDef.time_stamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=362,
  serialized_end=439,
)


_HEARTBEATREQUESTDEF = _descriptor.Descriptor(
  name='HeartBeatRequestDef',
  full_name='node.HeartBeatRequestDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='node.HeartBeatRequestDef.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='node.HeartBeatRequestDef.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='node.HeartBeatRequestDef.time_stamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=441,
  serialized_end=518,
)


_HEARTBEATRESPONSEDEF = _descriptor.Descriptor(
  name='HeartBeatResponseDef',
  full_name='node.HeartBeatResponseDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='node.HeartBeatResponseDef.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='node.HeartBeatResponseDef.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='node.HeartBeatResponseDef.time_stamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=520,
  serialized_end=598,
)


_REQUESTHEARTBEATREQUESTDEF = _descriptor.Descriptor(
  name='RequestHeartBeatRequestDef',
  full_name='node.RequestHeartBeatRequestDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='node.RequestHeartBeatRequestDef.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination_node_id', full_name='node.RequestHeartBeatRequestDef.destination_node_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='node.RequestHeartBeatRequestDef.time_stamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=600,
  serialized_end=697,
)


_REQUESTHEARTBEATRESPONSEDEF = _descriptor.Descriptor(
  name='RequestHeartBeatResponseDef',
  full_name='node.RequestHeartBeatResponseDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='node.RequestHeartBeatResponseDef.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='node.RequestHeartBeatResponseDef.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='node.RequestHeartBeatResponseDef.time_stamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=699,
  serialized_end=784,
)


_NODESSTATUSREQUESTDEF = _descriptor.Descriptor(
  name='NodesStatusRequestDef',
  full_name='node.NodesStatusRequestDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='node.NodesStatusRequestDef.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='node.NodesStatusRequestDef.time_stamp', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=786,
  serialized_end=849,
)


_NODESSTATUSRESPONSEDEF = _descriptor.Descriptor(
  name='NodesStatusResponseDef',
  full_name='node.NodesStatusResponseDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='node.NodesStatusResponseDef.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_list', full_name='node.NodesStatusResponseDef.node_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='node.NodesStatusResponseDef.time_stamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=851,
  serialized_end=946,
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
      number=3, type=1, cpp_type=5, label=1,
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
      name='is_leader', full_name='node.Node.is_leader', index=4,
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
  serialized_start=948,
  serialized_end=1034,
)

_ADDRESPONSEDEF.fields_by_name['node_list'].message_type = _NODE
_NODESSTATUSRESPONSEDEF.fields_by_name['node_list'].message_type = _NODE
DESCRIPTOR.message_types_by_name['AddRequestDef'] = _ADDREQUESTDEF
DESCRIPTOR.message_types_by_name['AddResponseDef'] = _ADDRESPONSEDEF
DESCRIPTOR.message_types_by_name['DiffNodeRequestDef'] = _DIFFNODEREQUESTDEF
DESCRIPTOR.message_types_by_name['DiffNodeResponseDef'] = _DIFFNODERESPONSEDEF
DESCRIPTOR.message_types_by_name['HeartBeatRequestDef'] = _HEARTBEATREQUESTDEF
DESCRIPTOR.message_types_by_name['HeartBeatResponseDef'] = _HEARTBEATRESPONSEDEF
DESCRIPTOR.message_types_by_name['RequestHeartBeatRequestDef'] = _REQUESTHEARTBEATREQUESTDEF
DESCRIPTOR.message_types_by_name['RequestHeartBeatResponseDef'] = _REQUESTHEARTBEATRESPONSEDEF
DESCRIPTOR.message_types_by_name['NodesStatusRequestDef'] = _NODESSTATUSREQUESTDEF
DESCRIPTOR.message_types_by_name['NodesStatusResponseDef'] = _NODESSTATUSRESPONSEDEF
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

DiffNodeRequestDef = _reflection.GeneratedProtocolMessageType('DiffNodeRequestDef', (_message.Message,), {
  'DESCRIPTOR' : _DIFFNODEREQUESTDEF,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:node.DiffNodeRequestDef)
  })
_sym_db.RegisterMessage(DiffNodeRequestDef)

DiffNodeResponseDef = _reflection.GeneratedProtocolMessageType('DiffNodeResponseDef', (_message.Message,), {
  'DESCRIPTOR' : _DIFFNODERESPONSEDEF,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:node.DiffNodeResponseDef)
  })
_sym_db.RegisterMessage(DiffNodeResponseDef)

HeartBeatRequestDef = _reflection.GeneratedProtocolMessageType('HeartBeatRequestDef', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATREQUESTDEF,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:node.HeartBeatRequestDef)
  })
_sym_db.RegisterMessage(HeartBeatRequestDef)

HeartBeatResponseDef = _reflection.GeneratedProtocolMessageType('HeartBeatResponseDef', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATRESPONSEDEF,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:node.HeartBeatResponseDef)
  })
_sym_db.RegisterMessage(HeartBeatResponseDef)

RequestHeartBeatRequestDef = _reflection.GeneratedProtocolMessageType('RequestHeartBeatRequestDef', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTHEARTBEATREQUESTDEF,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:node.RequestHeartBeatRequestDef)
  })
_sym_db.RegisterMessage(RequestHeartBeatRequestDef)

RequestHeartBeatResponseDef = _reflection.GeneratedProtocolMessageType('RequestHeartBeatResponseDef', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTHEARTBEATRESPONSEDEF,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:node.RequestHeartBeatResponseDef)
  })
_sym_db.RegisterMessage(RequestHeartBeatResponseDef)

NodesStatusRequestDef = _reflection.GeneratedProtocolMessageType('NodesStatusRequestDef', (_message.Message,), {
  'DESCRIPTOR' : _NODESSTATUSREQUESTDEF,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:node.NodesStatusRequestDef)
  })
_sym_db.RegisterMessage(NodesStatusRequestDef)

NodesStatusResponseDef = _reflection.GeneratedProtocolMessageType('NodesStatusResponseDef', (_message.Message,), {
  'DESCRIPTOR' : _NODESSTATUSRESPONSEDEF,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:node.NodesStatusResponseDef)
  })
_sym_db.RegisterMessage(NodesStatusResponseDef)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:node.Node)
  })
_sym_db.RegisterMessage(Node)



_REQUESTSERVICE = _descriptor.ServiceDescriptor(
  name='RequestService',
  full_name='node.RequestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1037,
  serialized_end=1449,
  methods=[
  _descriptor.MethodDescriptor(
    name='add_request',
    full_name='node.RequestService.add_request',
    index=0,
    containing_service=None,
    input_type=_ADDREQUESTDEF,
    output_type=_ADDRESPONSEDEF,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update_request',
    full_name='node.RequestService.update_request',
    index=1,
    containing_service=None,
    input_type=_DIFFNODEREQUESTDEF,
    output_type=_DIFFNODERESPONSEDEF,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='heartbeat_request',
    full_name='node.RequestService.heartbeat_request',
    index=2,
    containing_service=None,
    input_type=_HEARTBEATREQUESTDEF,
    output_type=_HEARTBEATRESPONSEDEF,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='request_heartbeat_request',
    full_name='node.RequestService.request_heartbeat_request',
    index=3,
    containing_service=None,
    input_type=_REQUESTHEARTBEATREQUESTDEF,
    output_type=_REQUESTHEARTBEATRESPONSEDEF,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='nodes_status_request',
    full_name='node.RequestService.nodes_status_request',
    index=4,
    containing_service=None,
    input_type=_NODESSTATUSREQUESTDEF,
    output_type=_NODESSTATUSRESPONSEDEF,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REQUESTSERVICE)

DESCRIPTOR.services_by_name['RequestService'] = _REQUESTSERVICE

# @@protoc_insertion_point(module_scope)
