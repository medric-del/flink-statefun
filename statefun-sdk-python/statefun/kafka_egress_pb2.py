# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kafka-egress.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12kafka-egress.proto\x12\x16io.statefun.sdk.egress\"F\n\x13KafkaProducerRecord\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x13\n\x0bvalue_bytes\x18\x02 \x01(\x0c\x12\r\n\x05topic\x18\x03 \x01(\tB>\n.org.apache.flink.statefun.sdk.egress.generatedP\x01Z\n.;protocolb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kafka_egress_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n.org.apache.flink.statefun.sdk.egress.generatedP\001Z\n.;protocol'
  _globals['_KAFKAPRODUCERRECORD']._serialized_start=46
  _globals['_KAFKAPRODUCERRECORD']._serialized_end=116
# @@protoc_insertion_point(module_scope)