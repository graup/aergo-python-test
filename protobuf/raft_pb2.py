# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import p2p_pb2 as p2p__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='raft.proto',
  package='types',
  syntax='proto3',
  serialized_options=_b('Z\036github.com/aergoio/aergo/types'),
  serialized_pb=_b('\n\nraft.proto\x12\x05types\x1a\tp2p.proto\"C\n\nMemberAttr\x12\n\n\x02ID\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0e\n\x06peerID\x18\x04 \x01(\x0c\"^\n\x10MembershipChange\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.types.MembershipChangeType\x12\x1f\n\x04\x61ttr\x18\x02 \x01(\x0b\x32\x11.types.MemberAttr\"8\n\x15MembershipChangeReply\x12\x1f\n\x04\x61ttr\x18\x01 \x01(\x0b\x32\x11.types.MemberAttr\"-\n\rHardStateInfo\x12\x0c\n\x04term\x18\x01 \x01(\x04\x12\x0e\n\x06\x63ommit\x18\x02 \x01(\x04\".\n\x15GetClusterInfoRequest\x12\x15\n\rbestBlockHash\x18\x01 \x01(\x0c\"\x8a\x01\n\x16GetClusterInfoResponse\x12\x0f\n\x07\x63hainID\x18\x01 \x01(\x0c\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12#\n\x08mbrAttrs\x18\x03 \x03(\x0b\x32\x11.types.MemberAttr\x12+\n\rhardStateInfo\x18\x04 \x01(\x0b\x32\x14.types.HardStateInfo*9\n\x14MembershipChangeType\x12\x0e\n\nADD_MEMBER\x10\x00\x12\x11\n\rREMOVE_MEMBER\x10\x01\x42 Z\x1egithub.com/aergoio/aergo/typesb\x06proto3')
  ,
  dependencies=[p2p__pb2.DESCRIPTOR,])

_MEMBERSHIPCHANGETYPE = _descriptor.EnumDescriptor(
  name='MembershipChangeType',
  full_name='types.MembershipChangeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD_MEMBER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_MEMBER', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=491,
  serialized_end=548,
)
_sym_db.RegisterEnumDescriptor(_MEMBERSHIPCHANGETYPE)

MembershipChangeType = enum_type_wrapper.EnumTypeWrapper(_MEMBERSHIPCHANGETYPE)
ADD_MEMBER = 0
REMOVE_MEMBER = 1



_MEMBERATTR = _descriptor.Descriptor(
  name='MemberAttr',
  full_name='types.MemberAttr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='types.MemberAttr.ID', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='types.MemberAttr.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='types.MemberAttr.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peerID', full_name='types.MemberAttr.peerID', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
  serialized_start=32,
  serialized_end=99,
)


_MEMBERSHIPCHANGE = _descriptor.Descriptor(
  name='MembershipChange',
  full_name='types.MembershipChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='types.MembershipChange.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attr', full_name='types.MembershipChange.attr', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=101,
  serialized_end=195,
)


_MEMBERSHIPCHANGEREPLY = _descriptor.Descriptor(
  name='MembershipChangeReply',
  full_name='types.MembershipChangeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attr', full_name='types.MembershipChangeReply.attr', index=0,
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
  serialized_start=197,
  serialized_end=253,
)


_HARDSTATEINFO = _descriptor.Descriptor(
  name='HardStateInfo',
  full_name='types.HardStateInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='term', full_name='types.HardStateInfo.term', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit', full_name='types.HardStateInfo.commit', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=255,
  serialized_end=300,
)


_GETCLUSTERINFOREQUEST = _descriptor.Descriptor(
  name='GetClusterInfoRequest',
  full_name='types.GetClusterInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bestBlockHash', full_name='types.GetClusterInfoRequest.bestBlockHash', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=302,
  serialized_end=348,
)


_GETCLUSTERINFORESPONSE = _descriptor.Descriptor(
  name='GetClusterInfoResponse',
  full_name='types.GetClusterInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chainID', full_name='types.GetClusterInfoResponse.chainID', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='types.GetClusterInfoResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mbrAttrs', full_name='types.GetClusterInfoResponse.mbrAttrs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hardStateInfo', full_name='types.GetClusterInfoResponse.hardStateInfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=351,
  serialized_end=489,
)

_MEMBERSHIPCHANGE.fields_by_name['type'].enum_type = _MEMBERSHIPCHANGETYPE
_MEMBERSHIPCHANGE.fields_by_name['attr'].message_type = _MEMBERATTR
_MEMBERSHIPCHANGEREPLY.fields_by_name['attr'].message_type = _MEMBERATTR
_GETCLUSTERINFORESPONSE.fields_by_name['mbrAttrs'].message_type = _MEMBERATTR
_GETCLUSTERINFORESPONSE.fields_by_name['hardStateInfo'].message_type = _HARDSTATEINFO
DESCRIPTOR.message_types_by_name['MemberAttr'] = _MEMBERATTR
DESCRIPTOR.message_types_by_name['MembershipChange'] = _MEMBERSHIPCHANGE
DESCRIPTOR.message_types_by_name['MembershipChangeReply'] = _MEMBERSHIPCHANGEREPLY
DESCRIPTOR.message_types_by_name['HardStateInfo'] = _HARDSTATEINFO
DESCRIPTOR.message_types_by_name['GetClusterInfoRequest'] = _GETCLUSTERINFOREQUEST
DESCRIPTOR.message_types_by_name['GetClusterInfoResponse'] = _GETCLUSTERINFORESPONSE
DESCRIPTOR.enum_types_by_name['MembershipChangeType'] = _MEMBERSHIPCHANGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MemberAttr = _reflection.GeneratedProtocolMessageType('MemberAttr', (_message.Message,), dict(
  DESCRIPTOR = _MEMBERATTR,
  __module__ = 'raft_pb2'
  # @@protoc_insertion_point(class_scope:types.MemberAttr)
  ))
_sym_db.RegisterMessage(MemberAttr)

MembershipChange = _reflection.GeneratedProtocolMessageType('MembershipChange', (_message.Message,), dict(
  DESCRIPTOR = _MEMBERSHIPCHANGE,
  __module__ = 'raft_pb2'
  # @@protoc_insertion_point(class_scope:types.MembershipChange)
  ))
_sym_db.RegisterMessage(MembershipChange)

MembershipChangeReply = _reflection.GeneratedProtocolMessageType('MembershipChangeReply', (_message.Message,), dict(
  DESCRIPTOR = _MEMBERSHIPCHANGEREPLY,
  __module__ = 'raft_pb2'
  # @@protoc_insertion_point(class_scope:types.MembershipChangeReply)
  ))
_sym_db.RegisterMessage(MembershipChangeReply)

HardStateInfo = _reflection.GeneratedProtocolMessageType('HardStateInfo', (_message.Message,), dict(
  DESCRIPTOR = _HARDSTATEINFO,
  __module__ = 'raft_pb2'
  # @@protoc_insertion_point(class_scope:types.HardStateInfo)
  ))
_sym_db.RegisterMessage(HardStateInfo)

GetClusterInfoRequest = _reflection.GeneratedProtocolMessageType('GetClusterInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCLUSTERINFOREQUEST,
  __module__ = 'raft_pb2'
  # @@protoc_insertion_point(class_scope:types.GetClusterInfoRequest)
  ))
_sym_db.RegisterMessage(GetClusterInfoRequest)

GetClusterInfoResponse = _reflection.GeneratedProtocolMessageType('GetClusterInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETCLUSTERINFORESPONSE,
  __module__ = 'raft_pb2'
  # @@protoc_insertion_point(class_scope:types.GetClusterInfoResponse)
  ))
_sym_db.RegisterMessage(GetClusterInfoResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
