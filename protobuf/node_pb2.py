# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='node.proto',
  package='types',
  syntax='proto3',
  serialized_options=_b('Z\036github.com/aergoio/aergo/types'),
  serialized_pb=_b('\n\nnode.proto\x12\x05types\"<\n\x0bPeerAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x0e\n\x06peerID\x18\x03 \x01(\x0c\x42 Z\x1egithub.com/aergoio/aergo/typesb\x06proto3')
)




_PEERADDRESS = _descriptor.Descriptor(
  name='PeerAddress',
  full_name='types.PeerAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='types.PeerAddress.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='types.PeerAddress.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peerID', full_name='types.PeerAddress.peerID', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=21,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['PeerAddress'] = _PEERADDRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PeerAddress = _reflection.GeneratedProtocolMessageType('PeerAddress', (_message.Message,), dict(
  DESCRIPTOR = _PEERADDRESS,
  __module__ = 'node_pb2'
  # @@protoc_insertion_point(class_scope:types.PeerAddress)
  ))
_sym_db.RegisterMessage(PeerAddress)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
