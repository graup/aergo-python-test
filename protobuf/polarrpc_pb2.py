# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: polarrpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import node_pb2 as node__pb2
import rpc_pb2 as rpc__pb2
import metric_pb2 as metric__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='polarrpc.proto',
  package='types',
  syntax='proto3',
  serialized_options=_b('Z\036github.com/aergoio/aergo/types'),
  serialized_pb=_b('\n\x0epolarrpc.proto\x12\x05types\x1a\nnode.proto\x1a\trpc.proto\x1a\x0cmetric.proto\"(\n\x0bPaginations\x12\x0b\n\x03ref\x18\x01 \x01(\x0c\x12\x0c\n\x04size\x18\x03 \x01(\r\"T\n\x0fPolarisPeerList\x12\r\n\x05total\x18\x01 \x01(\r\x12\x0f\n\x07hasNext\x18\x02 \x01(\x08\x12!\n\x05peers\x18\x03 \x03(\x0b\x32\x12.types.PolarisPeer\"h\n\x0bPolarisPeer\x12#\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x12.types.PeerAddress\x12\x11\n\tconnected\x18\x02 \x01(\x03\x12\x11\n\tlastCheck\x18\x03 \x01(\x03\x12\x0e\n\x06verion\x18\x04 \x01(\t2\xac\x02\n\x11PolarisRPCService\x12\x31\n\tNodeState\x12\x0e.types.NodeReq\x1a\x12.types.SingleBytes\"\x00\x12\x31\n\x06Metric\x12\x15.types.MetricsRequest\x1a\x0e.types.Metrics\"\x00\x12;\n\x0b\x43urrentList\x12\x12.types.Paginations\x1a\x16.types.PolarisPeerList\"\x00\x12\x39\n\tWhiteList\x12\x12.types.Paginations\x1a\x16.types.PolarisPeerList\"\x00\x12\x39\n\tBlackList\x12\x12.types.Paginations\x1a\x16.types.PolarisPeerList\"\x00\x42 Z\x1egithub.com/aergoio/aergo/typesb\x06proto3')
  ,
  dependencies=[node__pb2.DESCRIPTOR,rpc__pb2.DESCRIPTOR,metric__pb2.DESCRIPTOR,])




_PAGINATIONS = _descriptor.Descriptor(
  name='Paginations',
  full_name='types.Paginations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ref', full_name='types.Paginations.ref', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='types.Paginations.size', index=1,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=62,
  serialized_end=102,
)


_POLARISPEERLIST = _descriptor.Descriptor(
  name='PolarisPeerList',
  full_name='types.PolarisPeerList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='types.PolarisPeerList.total', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hasNext', full_name='types.PolarisPeerList.hasNext', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peers', full_name='types.PolarisPeerList.peers', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=104,
  serialized_end=188,
)


_POLARISPEER = _descriptor.Descriptor(
  name='PolarisPeer',
  full_name='types.PolarisPeer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='types.PolarisPeer.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connected', full_name='types.PolarisPeer.connected', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastCheck', full_name='types.PolarisPeer.lastCheck', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verion', full_name='types.PolarisPeer.verion', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=190,
  serialized_end=294,
)

_POLARISPEERLIST.fields_by_name['peers'].message_type = _POLARISPEER
_POLARISPEER.fields_by_name['address'].message_type = node__pb2._PEERADDRESS
DESCRIPTOR.message_types_by_name['Paginations'] = _PAGINATIONS
DESCRIPTOR.message_types_by_name['PolarisPeerList'] = _POLARISPEERLIST
DESCRIPTOR.message_types_by_name['PolarisPeer'] = _POLARISPEER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Paginations = _reflection.GeneratedProtocolMessageType('Paginations', (_message.Message,), dict(
  DESCRIPTOR = _PAGINATIONS,
  __module__ = 'polarrpc_pb2'
  # @@protoc_insertion_point(class_scope:types.Paginations)
  ))
_sym_db.RegisterMessage(Paginations)

PolarisPeerList = _reflection.GeneratedProtocolMessageType('PolarisPeerList', (_message.Message,), dict(
  DESCRIPTOR = _POLARISPEERLIST,
  __module__ = 'polarrpc_pb2'
  # @@protoc_insertion_point(class_scope:types.PolarisPeerList)
  ))
_sym_db.RegisterMessage(PolarisPeerList)

PolarisPeer = _reflection.GeneratedProtocolMessageType('PolarisPeer', (_message.Message,), dict(
  DESCRIPTOR = _POLARISPEER,
  __module__ = 'polarrpc_pb2'
  # @@protoc_insertion_point(class_scope:types.PolarisPeer)
  ))
_sym_db.RegisterMessage(PolarisPeer)


DESCRIPTOR._options = None

_POLARISRPCSERVICE = _descriptor.ServiceDescriptor(
  name='PolarisRPCService',
  full_name='types.PolarisRPCService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=297,
  serialized_end=597,
  methods=[
  _descriptor.MethodDescriptor(
    name='NodeState',
    full_name='types.PolarisRPCService.NodeState',
    index=0,
    containing_service=None,
    input_type=rpc__pb2._NODEREQ,
    output_type=rpc__pb2._SINGLEBYTES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Metric',
    full_name='types.PolarisRPCService.Metric',
    index=1,
    containing_service=None,
    input_type=metric__pb2._METRICSREQUEST,
    output_type=metric__pb2._METRICS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CurrentList',
    full_name='types.PolarisRPCService.CurrentList',
    index=2,
    containing_service=None,
    input_type=_PAGINATIONS,
    output_type=_POLARISPEERLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WhiteList',
    full_name='types.PolarisRPCService.WhiteList',
    index=3,
    containing_service=None,
    input_type=_PAGINATIONS,
    output_type=_POLARISPEERLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BlackList',
    full_name='types.PolarisRPCService.BlackList',
    index=4,
    containing_service=None,
    input_type=_PAGINATIONS,
    output_type=_POLARISPEERLIST,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_POLARISRPCSERVICE)

DESCRIPTOR.services_by_name['PolarisRPCService'] = _POLARISRPCSERVICE

# @@protoc_insertion_point(module_scope)
