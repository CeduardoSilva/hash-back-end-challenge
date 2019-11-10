# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: individualdiscount.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='individualdiscount.proto',
  package='individualdiscount',
  syntax='proto3',
  serialized_options=_b('\n-io.hash-back-end-challenge.individualdiscountB\027IndividualDiscountProtoP\001\242\002\010Ind-Disc'),
  serialized_pb=_b('\n\x18individualdiscount.proto\x12\x12individualdiscount\">\n\x19IndividualDiscountRequest\x12\x11\n\tproductId\x18\x01 \x01(\t\x12\x0e\n\x06userId\x18\x02 \x01(\t\"\\\n\x17IndividualDiscountReply\x12\x0b\n\x03pct\x18\x01 \x01(\x02\x12\x16\n\x0evalue_in_cents\x18\x02 \x01(\x05\x12\x1c\n\x14\x61pplicable_discounts\x18\x03 \x01(\t2~\n\x08\x44iscount\x12r\n\x12IndividualDiscount\x12-.individualdiscount.IndividualDiscountRequest\x1a+.individualdiscount.IndividualDiscountReply\"\x00\x42U\n-io.hash-back-end-challenge.individualdiscountB\x17IndividualDiscountProtoP\x01\xa2\x02\x08Ind-Discb\x06proto3')
)




_INDIVIDUALDISCOUNTREQUEST = _descriptor.Descriptor(
  name='IndividualDiscountRequest',
  full_name='individualdiscount.IndividualDiscountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='productId', full_name='individualdiscount.IndividualDiscountRequest.productId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userId', full_name='individualdiscount.IndividualDiscountRequest.userId', index=1,
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
  serialized_start=48,
  serialized_end=110,
)


_INDIVIDUALDISCOUNTREPLY = _descriptor.Descriptor(
  name='IndividualDiscountReply',
  full_name='individualdiscount.IndividualDiscountReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pct', full_name='individualdiscount.IndividualDiscountReply.pct', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_in_cents', full_name='individualdiscount.IndividualDiscountReply.value_in_cents', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='applicable_discounts', full_name='individualdiscount.IndividualDiscountReply.applicable_discounts', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=112,
  serialized_end=204,
)

DESCRIPTOR.message_types_by_name['IndividualDiscountRequest'] = _INDIVIDUALDISCOUNTREQUEST
DESCRIPTOR.message_types_by_name['IndividualDiscountReply'] = _INDIVIDUALDISCOUNTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IndividualDiscountRequest = _reflection.GeneratedProtocolMessageType('IndividualDiscountRequest', (_message.Message,), {
  'DESCRIPTOR' : _INDIVIDUALDISCOUNTREQUEST,
  '__module__' : 'individualdiscount_pb2'
  # @@protoc_insertion_point(class_scope:individualdiscount.IndividualDiscountRequest)
  })
_sym_db.RegisterMessage(IndividualDiscountRequest)

IndividualDiscountReply = _reflection.GeneratedProtocolMessageType('IndividualDiscountReply', (_message.Message,), {
  'DESCRIPTOR' : _INDIVIDUALDISCOUNTREPLY,
  '__module__' : 'individualdiscount_pb2'
  # @@protoc_insertion_point(class_scope:individualdiscount.IndividualDiscountReply)
  })
_sym_db.RegisterMessage(IndividualDiscountReply)


DESCRIPTOR._options = None

_DISCOUNT = _descriptor.ServiceDescriptor(
  name='Discount',
  full_name='individualdiscount.Discount',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=206,
  serialized_end=332,
  methods=[
  _descriptor.MethodDescriptor(
    name='IndividualDiscount',
    full_name='individualdiscount.Discount.IndividualDiscount',
    index=0,
    containing_service=None,
    input_type=_INDIVIDUALDISCOUNTREQUEST,
    output_type=_INDIVIDUALDISCOUNTREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISCOUNT)

DESCRIPTOR.services_by_name['Discount'] = _DISCOUNT

# @@protoc_insertion_point(module_scope)
