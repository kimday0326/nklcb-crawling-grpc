# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crawling_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63rawling_service.proto\"5\n\x0f\x43rawlingRequest\x12\x0f\n\x07rss_url\x18\x01 \x01(\t\x12\x11\n\tbase_time\x18\x02 \x01(\t\".\n\x10\x43rawlingResponse\x12\x1a\n\x08\x61rticles\x18\x01 \x03(\x0b\x32\x08.Article\"\x7f\n\x07\x41rticle\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x04 \x01(\t\x12\x0c\n\x04link\x18\x05 \x01(\t\x12\x13\n\x0bpublishedAt\x18\x06 \x01(\t\x12\x10\n\x08keywords\x18\x07 \x03(\t2A\n\x0f\x43rawlingService\x12.\n\x05\x43rawl\x12\x10.CrawlingRequest\x1a\x11.CrawlingResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crawling_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CRAWLINGREQUEST']._serialized_start=26
  _globals['_CRAWLINGREQUEST']._serialized_end=79
  _globals['_CRAWLINGRESPONSE']._serialized_start=81
  _globals['_CRAWLINGRESPONSE']._serialized_end=127
  _globals['_ARTICLE']._serialized_start=129
  _globals['_ARTICLE']._serialized_end=256
  _globals['_CRAWLINGSERVICE']._serialized_start=258
  _globals['_CRAWLINGSERVICE']._serialized_end=323
# @@protoc_insertion_point(module_scope)
