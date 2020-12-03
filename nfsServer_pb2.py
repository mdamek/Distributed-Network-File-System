# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nfsServer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nfsServer.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fnfsServer.proto\"\x14\n\x04Path\x12\x0c\n\x04path\x18\x01 \x01(\t\"<\n\x15SourceDestinationPath\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\"\x14\n\x06Result\x12\n\n\x02\x65x\x18\x01 \x01(\t\">\n\x0e\x46olderContents\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0f\n\x07\x66olders\x18\x02 \x01(\t\x12\r\n\x05\x66iles\x18\x03 \x01(\t2\xcd\x03\n\tNFSServer\x12)\n\rListDirectory\x12\x05.Path\x1a\x0f.FolderContents\"\x00\x12#\n\x0f\x44\x65leteDirectory\x12\x05.Path\x1a\x07.Result\"\x00\x12#\n\x0f\x43reateDirectory\x12\x05.Path\x1a\x07.Result\"\x00\x12\x32\n\rMoveDirectory\x12\x16.SourceDestinationPath\x1a\x07.Result\"\x00\x12\x32\n\rCopyDirectory\x12\x16.SourceDestinationPath\x1a\x07.Result\"\x00\x12\x34\n\x0fRenameDirectory\x12\x16.SourceDestinationPath\x1a\x07.Result\"\x00\x12/\n\nRenameFile\x12\x16.SourceDestinationPath\x1a\x07.Result\"\x00\x12-\n\x08MoveFile\x12\x16.SourceDestinationPath\x1a\x07.Result\"\x00\x12-\n\x08\x43opyFile\x12\x16.SourceDestinationPath\x1a\x07.Result\"\x00\x12\x1e\n\nDeleteFile\x12\x05.Path\x1a\x07.Result\"\x00\x62\x06proto3'
)




_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='Path.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=19,
  serialized_end=39,
)


_SOURCEDESTINATIONPATH = _descriptor.Descriptor(
  name='SourceDestinationPath',
  full_name='SourceDestinationPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='SourceDestinationPath.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination', full_name='SourceDestinationPath.destination', index=1,
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
  serialized_start=41,
  serialized_end=101,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ex', full_name='Result.ex', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=103,
  serialized_end=123,
)


_FOLDERCONTENTS = _descriptor.Descriptor(
  name='FolderContents',
  full_name='FolderContents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='FolderContents.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folders', full_name='FolderContents.folders', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='files', full_name='FolderContents.files', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=125,
  serialized_end=187,
)

DESCRIPTOR.message_types_by_name['Path'] = _PATH
DESCRIPTOR.message_types_by_name['SourceDestinationPath'] = _SOURCEDESTINATIONPATH
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['FolderContents'] = _FOLDERCONTENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), {
  'DESCRIPTOR' : _PATH,
  '__module__' : 'nfsServer_pb2'
  # @@protoc_insertion_point(class_scope:Path)
  })
_sym_db.RegisterMessage(Path)

SourceDestinationPath = _reflection.GeneratedProtocolMessageType('SourceDestinationPath', (_message.Message,), {
  'DESCRIPTOR' : _SOURCEDESTINATIONPATH,
  '__module__' : 'nfsServer_pb2'
  # @@protoc_insertion_point(class_scope:SourceDestinationPath)
  })
_sym_db.RegisterMessage(SourceDestinationPath)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'nfsServer_pb2'
  # @@protoc_insertion_point(class_scope:Result)
  })
_sym_db.RegisterMessage(Result)

FolderContents = _reflection.GeneratedProtocolMessageType('FolderContents', (_message.Message,), {
  'DESCRIPTOR' : _FOLDERCONTENTS,
  '__module__' : 'nfsServer_pb2'
  # @@protoc_insertion_point(class_scope:FolderContents)
  })
_sym_db.RegisterMessage(FolderContents)



_NFSSERVER = _descriptor.ServiceDescriptor(
  name='NFSServer',
  full_name='NFSServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=190,
  serialized_end=651,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListDirectory',
    full_name='NFSServer.ListDirectory',
    index=0,
    containing_service=None,
    input_type=_PATH,
    output_type=_FOLDERCONTENTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteDirectory',
    full_name='NFSServer.DeleteDirectory',
    index=1,
    containing_service=None,
    input_type=_PATH,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateDirectory',
    full_name='NFSServer.CreateDirectory',
    index=2,
    containing_service=None,
    input_type=_PATH,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MoveDirectory',
    full_name='NFSServer.MoveDirectory',
    index=3,
    containing_service=None,
    input_type=_SOURCEDESTINATIONPATH,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CopyDirectory',
    full_name='NFSServer.CopyDirectory',
    index=4,
    containing_service=None,
    input_type=_SOURCEDESTINATIONPATH,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RenameDirectory',
    full_name='NFSServer.RenameDirectory',
    index=5,
    containing_service=None,
    input_type=_SOURCEDESTINATIONPATH,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RenameFile',
    full_name='NFSServer.RenameFile',
    index=6,
    containing_service=None,
    input_type=_SOURCEDESTINATIONPATH,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MoveFile',
    full_name='NFSServer.MoveFile',
    index=7,
    containing_service=None,
    input_type=_SOURCEDESTINATIONPATH,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CopyFile',
    full_name='NFSServer.CopyFile',
    index=8,
    containing_service=None,
    input_type=_SOURCEDESTINATIONPATH,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteFile',
    full_name='NFSServer.DeleteFile',
    index=9,
    containing_service=None,
    input_type=_PATH,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NFSSERVER)

DESCRIPTOR.services_by_name['NFSServer'] = _NFSSERVER

# @@protoc_insertion_point(module_scope)
