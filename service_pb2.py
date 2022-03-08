# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rservice.proto\"q\n\x10InferenceRequest\x12\x12\n\nfile_paths\x18\x01 \x03(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x1d\n\x15original_image_height\x18\x03 \x01(\x05\x12\x1c\n\x14original_image_width\x18\x04 \x01(\x05\"{\n\x0b\x42oundingBox\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x10\n\x08\x63lass_id\x18\x02 \x01(\x05\x12\r\n\x05score\x18\x03 \x01(\x02\x12\x0c\n\x04left\x18\x04 \x01(\x02\x12\x0b\n\x03top\x18\x05 \x01(\x02\x12\r\n\x05width\x18\x06 \x01(\x02\x12\x0e\n\x06height\x18\x07 \x01(\x02\"@\n\x0eInferenceReply\x12 \n\ndetections\x18\x01 \x03(\x0b\x32\x0c.BoundingBox\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"^\n\rTrackerResult\x12\x1f\n\tdetection\x18\x01 \x01(\x0b\x32\x0c.BoundingBox\x12\x13\n\x0bsequence_id\x18\x02 \x01(\x03\x12\x17\n\x0fsequence_length\x18\x03 \x01(\x03\"L\n\x0eTrackerResults\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\'\n\x0ftracker_results\x18\x02 \x03(\x0b\x32\x0e.TrackerResult2=\n\x08\x44\x65tector\x12\x31\n\tInference\x12\x11.InferenceRequest\x1a\x0f.InferenceReply\"\x00\x62\x06proto3'
)




_INFERENCEREQUEST = _descriptor.Descriptor(
  name='InferenceRequest',
  full_name='InferenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_paths', full_name='InferenceRequest.file_paths', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='InferenceRequest.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='original_image_height', full_name='InferenceRequest.original_image_height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='original_image_width', full_name='InferenceRequest.original_image_width', index=3,
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
  serialized_start=17,
  serialized_end=130,
)


_BOUNDINGBOX = _descriptor.Descriptor(
  name='BoundingBox',
  full_name='BoundingBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_path', full_name='BoundingBox.file_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='class_id', full_name='BoundingBox.class_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='BoundingBox.score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='left', full_name='BoundingBox.left', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top', full_name='BoundingBox.top', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='BoundingBox.width', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='BoundingBox.height', index=6,
      number=7, type=2, cpp_type=6, label=1,
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
  serialized_start=132,
  serialized_end=255,
)


_INFERENCEREPLY = _descriptor.Descriptor(
  name='InferenceReply',
  full_name='InferenceReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='detections', full_name='InferenceReply.detections', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='InferenceReply.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=257,
  serialized_end=321,
)


_TRACKERRESULT = _descriptor.Descriptor(
  name='TrackerResult',
  full_name='TrackerResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='detection', full_name='TrackerResult.detection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_id', full_name='TrackerResult.sequence_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_length', full_name='TrackerResult.sequence_length', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=323,
  serialized_end=417,
)


_TRACKERRESULTS = _descriptor.Descriptor(
  name='TrackerResults',
  full_name='TrackerResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_path', full_name='TrackerResults.file_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tracker_results', full_name='TrackerResults.tracker_results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=419,
  serialized_end=495,
)

_INFERENCEREPLY.fields_by_name['detections'].message_type = _BOUNDINGBOX
_TRACKERRESULT.fields_by_name['detection'].message_type = _BOUNDINGBOX
_TRACKERRESULTS.fields_by_name['tracker_results'].message_type = _TRACKERRESULT
DESCRIPTOR.message_types_by_name['InferenceRequest'] = _INFERENCEREQUEST
DESCRIPTOR.message_types_by_name['BoundingBox'] = _BOUNDINGBOX
DESCRIPTOR.message_types_by_name['InferenceReply'] = _INFERENCEREPLY
DESCRIPTOR.message_types_by_name['TrackerResult'] = _TRACKERRESULT
DESCRIPTOR.message_types_by_name['TrackerResults'] = _TRACKERRESULTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InferenceRequest = _reflection.GeneratedProtocolMessageType('InferenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCEREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:InferenceRequest)
  })
_sym_db.RegisterMessage(InferenceRequest)

BoundingBox = _reflection.GeneratedProtocolMessageType('BoundingBox', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDINGBOX,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:BoundingBox)
  })
_sym_db.RegisterMessage(BoundingBox)

InferenceReply = _reflection.GeneratedProtocolMessageType('InferenceReply', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCEREPLY,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:InferenceReply)
  })
_sym_db.RegisterMessage(InferenceReply)

TrackerResult = _reflection.GeneratedProtocolMessageType('TrackerResult', (_message.Message,), {
  'DESCRIPTOR' : _TRACKERRESULT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:TrackerResult)
  })
_sym_db.RegisterMessage(TrackerResult)

TrackerResults = _reflection.GeneratedProtocolMessageType('TrackerResults', (_message.Message,), {
  'DESCRIPTOR' : _TRACKERRESULTS,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:TrackerResults)
  })
_sym_db.RegisterMessage(TrackerResults)



_DETECTOR = _descriptor.ServiceDescriptor(
  name='Detector',
  full_name='Detector',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=497,
  serialized_end=558,
  methods=[
  _descriptor.MethodDescriptor(
    name='Inference',
    full_name='Detector.Inference',
    index=0,
    containing_service=None,
    input_type=_INFERENCEREQUEST,
    output_type=_INFERENCEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DETECTOR)

DESCRIPTOR.services_by_name['Detector'] = _DETECTOR

# @@protoc_insertion_point(module_scope)
