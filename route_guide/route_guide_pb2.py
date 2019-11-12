# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: route_guide.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='route_guide.proto',
  package='route_guide',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11route_guide.proto\x12\x0broute_guide\",\n\x05Point\x12\x10\n\x08latitude\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\x05\"K\n\tRectangle\x12\x1e\n\x02lo\x18\x01 \x01(\x0b\x32\x12.route_guide.Point\x12\x1e\n\x02hi\x18\x02 \x01(\x0b\x32\x12.route_guide.Point\"=\n\x07\x46\x65\x61ture\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x08location\x18\x02 \x01(\x0b\x32\x12.route_guide.Point\"B\n\tRouteNote\x12$\n\x08location\x18\x01 \x01(\x0b\x32\x12.route_guide.Point\x12\x0f\n\x07message\x18\x02 \x01(\t\"b\n\x0cRouteSummary\x12\x13\n\x0bpoint_count\x18\x01 \x01(\x05\x12\x15\n\rfeature_count\x18\x02 \x01(\x05\x12\x10\n\x08\x64istance\x18\x03 \x01(\x05\x12\x14\n\x0c\x65lapsed_time\x18\x04 \x01(\x05\x32\x91\x02\n\nRouteGuide\x12\x39\n\x0bget_feature\x12\x12.route_guide.Point\x1a\x14.route_guide.Feature\"\x00\x12\x41\n\rlist_features\x12\x16.route_guide.Rectangle\x1a\x14.route_guide.Feature\"\x00\x30\x01\x12\x41\n\x0crecord_route\x12\x12.route_guide.Point\x1a\x19.route_guide.RouteSummary\"\x00(\x01\x12\x42\n\nroute_chat\x12\x16.route_guide.RouteNote\x1a\x16.route_guide.RouteNote\"\x00(\x01\x30\x01\x62\x06proto3'
)




_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='route_guide.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='route_guide.Point.latitude', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='route_guide.Point.longitude', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=34,
  serialized_end=78,
)


_RECTANGLE = _descriptor.Descriptor(
  name='Rectangle',
  full_name='route_guide.Rectangle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lo', full_name='route_guide.Rectangle.lo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hi', full_name='route_guide.Rectangle.hi', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=80,
  serialized_end=155,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='route_guide.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='route_guide.Feature.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='route_guide.Feature.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=157,
  serialized_end=218,
)


_ROUTENOTE = _descriptor.Descriptor(
  name='RouteNote',
  full_name='route_guide.RouteNote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='route_guide.RouteNote.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='route_guide.RouteNote.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=220,
  serialized_end=286,
)


_ROUTESUMMARY = _descriptor.Descriptor(
  name='RouteSummary',
  full_name='route_guide.RouteSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='point_count', full_name='route_guide.RouteSummary.point_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature_count', full_name='route_guide.RouteSummary.feature_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distance', full_name='route_guide.RouteSummary.distance', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='elapsed_time', full_name='route_guide.RouteSummary.elapsed_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=288,
  serialized_end=386,
)

_RECTANGLE.fields_by_name['lo'].message_type = _POINT
_RECTANGLE.fields_by_name['hi'].message_type = _POINT
_FEATURE.fields_by_name['location'].message_type = _POINT
_ROUTENOTE.fields_by_name['location'].message_type = _POINT
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Rectangle'] = _RECTANGLE
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['RouteNote'] = _ROUTENOTE
DESCRIPTOR.message_types_by_name['RouteSummary'] = _ROUTESUMMARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:route_guide.Point)
  })
_sym_db.RegisterMessage(Point)

Rectangle = _reflection.GeneratedProtocolMessageType('Rectangle', (_message.Message,), {
  'DESCRIPTOR' : _RECTANGLE,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:route_guide.Rectangle)
  })
_sym_db.RegisterMessage(Rectangle)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {
  'DESCRIPTOR' : _FEATURE,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:route_guide.Feature)
  })
_sym_db.RegisterMessage(Feature)

RouteNote = _reflection.GeneratedProtocolMessageType('RouteNote', (_message.Message,), {
  'DESCRIPTOR' : _ROUTENOTE,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:route_guide.RouteNote)
  })
_sym_db.RegisterMessage(RouteNote)

RouteSummary = _reflection.GeneratedProtocolMessageType('RouteSummary', (_message.Message,), {
  'DESCRIPTOR' : _ROUTESUMMARY,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:route_guide.RouteSummary)
  })
_sym_db.RegisterMessage(RouteSummary)



_ROUTEGUIDE = _descriptor.ServiceDescriptor(
  name='RouteGuide',
  full_name='route_guide.RouteGuide',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=389,
  serialized_end=662,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_feature',
    full_name='route_guide.RouteGuide.get_feature',
    index=0,
    containing_service=None,
    input_type=_POINT,
    output_type=_FEATURE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='list_features',
    full_name='route_guide.RouteGuide.list_features',
    index=1,
    containing_service=None,
    input_type=_RECTANGLE,
    output_type=_FEATURE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='record_route',
    full_name='route_guide.RouteGuide.record_route',
    index=2,
    containing_service=None,
    input_type=_POINT,
    output_type=_ROUTESUMMARY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='route_chat',
    full_name='route_guide.RouteGuide.route_chat',
    index=3,
    containing_service=None,
    input_type=_ROUTENOTE,
    output_type=_ROUTENOTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROUTEGUIDE)

DESCRIPTOR.services_by_name['RouteGuide'] = _ROUTEGUIDE

# @@protoc_insertion_point(module_scope)