# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/faucet_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from forch.proto import shared_constants_pb2 as forch_dot_proto_dot_shared__constants__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/faucet_event.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x1e\x66orch/proto/faucet_event.proto\x1a\"forch/proto/shared_constants.proto\"\xf4\x01\n\x0b\x46\x61ucetEvent\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x02\x12\x0f\n\x07\x64p_name\x18\x03 \x01(\t\x12\r\n\x05\x64p_id\x18\x04 \x01(\x03\x12\x10\n\x08\x65vent_id\x18\x05 \x01(\x05\x12\x11\n\tdebounced\x18\x06 \x01(\x08\x12 \n\nLAG_CHANGE\x18\x07 \x01(\x0b\x32\n.LagChangeH\x00\x12\"\n\x0bSTACK_STATE\x18\t \x01(\x0b\x32\x0b.StackStateH\x00\x12-\n\x11STACK_TOPO_CHANGE\x18\x08 \x01(\x0b\x32\x10.StackTopoChangeH\x00\x42\x0c\n\nevent_data\"O\n\tLagChange\x12\x11\n\ttimestamp\x18\x01 \x01(\x02\x12\x0f\n\x07\x64p_name\x18\x02 \x01(\t\x12\x0f\n\x07port_no\x18\x03 \x01(\x05\x12\r\n\x05state\x18\x04 \x01(\x05\"[\n\nStackState\x12\x11\n\ttimestamp\x18\x01 \x01(\x02\x12\x0f\n\x07\x64p_name\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x1b\n\x05state\x18\x04 \x01(\x0e\x32\x0c.State.State\"\x8b\x05\n\x0fStackTopoChange\x12\x11\n\ttimestamp\x18\x01 \x01(\x02\x12\x12\n\nstack_root\x18\x02 \x01(\t\x12*\n\x05graph\x18\x03 \x01(\x0b\x32\x1b.StackTopoChange.StackGraph\x12&\n\x03\x64ps\x18\x04 \x03(\x0b\x32\x19.StackTopoChange.DpsEntry\x1a\x44\n\x08\x44psEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.StackTopoChange.StackDp:\x02\x38\x01\x1a\xb6\x01\n\nStackGraph\x12\x10\n\x08\x64irected\x18\x01 \x01(\x08\x12\x12\n\nmultigraph\x18\x02 \x01(\x08\x12,\n\x05graph\x18\x03 \x01(\x0b\x32\x1d.StackTopoChange.NetworkGraph\x12)\n\x05nodes\x18\x04 \x03(\x0b\x32\x1a.StackTopoChange.StackNode\x12)\n\x05links\x18\x05 \x03(\x0b\x32\x1a.StackTopoChange.StackLink\x1a\x0e\n\x0cNetworkGraph\x1a\x17\n\tStackNode\x12\n\n\x02id\x18\x01 \x01(\t\x1ah\n\tStackLink\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0e\n\x06target\x18\x03 \x01(\t\x12.\n\x08port_map\x18\x04 \x01(\x0b\x32\x1c.StackTopoChange.LinkPortMap\x1aI\n\x0bLinkPortMap\x12\x0c\n\x04\x64p_a\x18\x01 \x01(\t\x12\x0e\n\x06port_a\x18\x02 \x01(\t\x12\x0c\n\x04\x64p_z\x18\x03 \x01(\t\x12\x0e\n\x06port_z\x18\x04 \x01(\t\x1a \n\x07StackDp\x12\x15\n\rroot_hop_port\x18\x01 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[forch_dot_proto_dot_shared__constants__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FAUCETEVENT = _descriptor.Descriptor(
  name='FaucetEvent',
  full_name='FaucetEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='FaucetEvent.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='FaucetEvent.time', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dp_name', full_name='FaucetEvent.dp_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dp_id', full_name='FaucetEvent.dp_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='FaucetEvent.event_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debounced', full_name='FaucetEvent.debounced', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LAG_CHANGE', full_name='FaucetEvent.LAG_CHANGE', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='STACK_STATE', full_name='FaucetEvent.STACK_STATE', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='STACK_TOPO_CHANGE', full_name='FaucetEvent.STACK_TOPO_CHANGE', index=8,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='event_data', full_name='FaucetEvent.event_data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=71,
  serialized_end=315,
)


_LAGCHANGE = _descriptor.Descriptor(
  name='LagChange',
  full_name='LagChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='LagChange.timestamp', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dp_name', full_name='LagChange.dp_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port_no', full_name='LagChange.port_no', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='LagChange.state', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=396,
)


_STACKSTATE = _descriptor.Descriptor(
  name='StackState',
  full_name='StackState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='StackState.timestamp', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dp_name', full_name='StackState.dp_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='StackState.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='StackState.state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=398,
  serialized_end=489,
)


_STACKTOPOCHANGE_DPSENTRY = _descriptor.Descriptor(
  name='DpsEntry',
  full_name='StackTopoChange.DpsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='StackTopoChange.DpsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='StackTopoChange.DpsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=634,
  serialized_end=702,
)

_STACKTOPOCHANGE_STACKGRAPH = _descriptor.Descriptor(
  name='StackGraph',
  full_name='StackTopoChange.StackGraph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='directed', full_name='StackTopoChange.StackGraph.directed', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multigraph', full_name='StackTopoChange.StackGraph.multigraph', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graph', full_name='StackTopoChange.StackGraph.graph', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='StackTopoChange.StackGraph.nodes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='links', full_name='StackTopoChange.StackGraph.links', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=705,
  serialized_end=887,
)

_STACKTOPOCHANGE_NETWORKGRAPH = _descriptor.Descriptor(
  name='NetworkGraph',
  full_name='StackTopoChange.NetworkGraph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=889,
  serialized_end=903,
)

_STACKTOPOCHANGE_STACKNODE = _descriptor.Descriptor(
  name='StackNode',
  full_name='StackTopoChange.StackNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='StackTopoChange.StackNode.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=905,
  serialized_end=928,
)

_STACKTOPOCHANGE_STACKLINK = _descriptor.Descriptor(
  name='StackLink',
  full_name='StackTopoChange.StackLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='StackTopoChange.StackLink.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='StackTopoChange.StackLink.source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='StackTopoChange.StackLink.target', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port_map', full_name='StackTopoChange.StackLink.port_map', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=930,
  serialized_end=1034,
)

_STACKTOPOCHANGE_LINKPORTMAP = _descriptor.Descriptor(
  name='LinkPortMap',
  full_name='StackTopoChange.LinkPortMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dp_a', full_name='StackTopoChange.LinkPortMap.dp_a', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port_a', full_name='StackTopoChange.LinkPortMap.port_a', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dp_z', full_name='StackTopoChange.LinkPortMap.dp_z', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port_z', full_name='StackTopoChange.LinkPortMap.port_z', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1036,
  serialized_end=1109,
)

_STACKTOPOCHANGE_STACKDP = _descriptor.Descriptor(
  name='StackDp',
  full_name='StackTopoChange.StackDp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='root_hop_port', full_name='StackTopoChange.StackDp.root_hop_port', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1111,
  serialized_end=1143,
)

_STACKTOPOCHANGE = _descriptor.Descriptor(
  name='StackTopoChange',
  full_name='StackTopoChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='StackTopoChange.timestamp', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stack_root', full_name='StackTopoChange.stack_root', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graph', full_name='StackTopoChange.graph', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dps', full_name='StackTopoChange.dps', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STACKTOPOCHANGE_DPSENTRY, _STACKTOPOCHANGE_STACKGRAPH, _STACKTOPOCHANGE_NETWORKGRAPH, _STACKTOPOCHANGE_STACKNODE, _STACKTOPOCHANGE_STACKLINK, _STACKTOPOCHANGE_LINKPORTMAP, _STACKTOPOCHANGE_STACKDP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=1143,
)

_FAUCETEVENT.fields_by_name['LAG_CHANGE'].message_type = _LAGCHANGE
_FAUCETEVENT.fields_by_name['STACK_STATE'].message_type = _STACKSTATE
_FAUCETEVENT.fields_by_name['STACK_TOPO_CHANGE'].message_type = _STACKTOPOCHANGE
_FAUCETEVENT.oneofs_by_name['event_data'].fields.append(
  _FAUCETEVENT.fields_by_name['LAG_CHANGE'])
_FAUCETEVENT.fields_by_name['LAG_CHANGE'].containing_oneof = _FAUCETEVENT.oneofs_by_name['event_data']
_FAUCETEVENT.oneofs_by_name['event_data'].fields.append(
  _FAUCETEVENT.fields_by_name['STACK_STATE'])
_FAUCETEVENT.fields_by_name['STACK_STATE'].containing_oneof = _FAUCETEVENT.oneofs_by_name['event_data']
_FAUCETEVENT.oneofs_by_name['event_data'].fields.append(
  _FAUCETEVENT.fields_by_name['STACK_TOPO_CHANGE'])
_FAUCETEVENT.fields_by_name['STACK_TOPO_CHANGE'].containing_oneof = _FAUCETEVENT.oneofs_by_name['event_data']
_STACKSTATE.fields_by_name['state'].enum_type = forch_dot_proto_dot_shared__constants__pb2._STATE_STATE
_STACKTOPOCHANGE_DPSENTRY.fields_by_name['value'].message_type = _STACKTOPOCHANGE_STACKDP
_STACKTOPOCHANGE_DPSENTRY.containing_type = _STACKTOPOCHANGE
_STACKTOPOCHANGE_STACKGRAPH.fields_by_name['graph'].message_type = _STACKTOPOCHANGE_NETWORKGRAPH
_STACKTOPOCHANGE_STACKGRAPH.fields_by_name['nodes'].message_type = _STACKTOPOCHANGE_STACKNODE
_STACKTOPOCHANGE_STACKGRAPH.fields_by_name['links'].message_type = _STACKTOPOCHANGE_STACKLINK
_STACKTOPOCHANGE_STACKGRAPH.containing_type = _STACKTOPOCHANGE
_STACKTOPOCHANGE_NETWORKGRAPH.containing_type = _STACKTOPOCHANGE
_STACKTOPOCHANGE_STACKNODE.containing_type = _STACKTOPOCHANGE
_STACKTOPOCHANGE_STACKLINK.fields_by_name['port_map'].message_type = _STACKTOPOCHANGE_LINKPORTMAP
_STACKTOPOCHANGE_STACKLINK.containing_type = _STACKTOPOCHANGE
_STACKTOPOCHANGE_LINKPORTMAP.containing_type = _STACKTOPOCHANGE
_STACKTOPOCHANGE_STACKDP.containing_type = _STACKTOPOCHANGE
_STACKTOPOCHANGE.fields_by_name['graph'].message_type = _STACKTOPOCHANGE_STACKGRAPH
_STACKTOPOCHANGE.fields_by_name['dps'].message_type = _STACKTOPOCHANGE_DPSENTRY
DESCRIPTOR.message_types_by_name['FaucetEvent'] = _FAUCETEVENT
DESCRIPTOR.message_types_by_name['LagChange'] = _LAGCHANGE
DESCRIPTOR.message_types_by_name['StackState'] = _STACKSTATE
DESCRIPTOR.message_types_by_name['StackTopoChange'] = _STACKTOPOCHANGE

FaucetEvent = _reflection.GeneratedProtocolMessageType('FaucetEvent', (_message.Message,), dict(
  DESCRIPTOR = _FAUCETEVENT,
  __module__ = 'forch.proto.faucet_event_pb2'
  # @@protoc_insertion_point(class_scope:FaucetEvent)
  ))
_sym_db.RegisterMessage(FaucetEvent)

LagChange = _reflection.GeneratedProtocolMessageType('LagChange', (_message.Message,), dict(
  DESCRIPTOR = _LAGCHANGE,
  __module__ = 'forch.proto.faucet_event_pb2'
  # @@protoc_insertion_point(class_scope:LagChange)
  ))
_sym_db.RegisterMessage(LagChange)

StackState = _reflection.GeneratedProtocolMessageType('StackState', (_message.Message,), dict(
  DESCRIPTOR = _STACKSTATE,
  __module__ = 'forch.proto.faucet_event_pb2'
  # @@protoc_insertion_point(class_scope:StackState)
  ))
_sym_db.RegisterMessage(StackState)

StackTopoChange = _reflection.GeneratedProtocolMessageType('StackTopoChange', (_message.Message,), dict(

  DpsEntry = _reflection.GeneratedProtocolMessageType('DpsEntry', (_message.Message,), dict(
    DESCRIPTOR = _STACKTOPOCHANGE_DPSENTRY,
    __module__ = 'forch.proto.faucet_event_pb2'
    # @@protoc_insertion_point(class_scope:StackTopoChange.DpsEntry)
    ))
  ,

  StackGraph = _reflection.GeneratedProtocolMessageType('StackGraph', (_message.Message,), dict(
    DESCRIPTOR = _STACKTOPOCHANGE_STACKGRAPH,
    __module__ = 'forch.proto.faucet_event_pb2'
    # @@protoc_insertion_point(class_scope:StackTopoChange.StackGraph)
    ))
  ,

  NetworkGraph = _reflection.GeneratedProtocolMessageType('NetworkGraph', (_message.Message,), dict(
    DESCRIPTOR = _STACKTOPOCHANGE_NETWORKGRAPH,
    __module__ = 'forch.proto.faucet_event_pb2'
    # @@protoc_insertion_point(class_scope:StackTopoChange.NetworkGraph)
    ))
  ,

  StackNode = _reflection.GeneratedProtocolMessageType('StackNode', (_message.Message,), dict(
    DESCRIPTOR = _STACKTOPOCHANGE_STACKNODE,
    __module__ = 'forch.proto.faucet_event_pb2'
    # @@protoc_insertion_point(class_scope:StackTopoChange.StackNode)
    ))
  ,

  StackLink = _reflection.GeneratedProtocolMessageType('StackLink', (_message.Message,), dict(
    DESCRIPTOR = _STACKTOPOCHANGE_STACKLINK,
    __module__ = 'forch.proto.faucet_event_pb2'
    # @@protoc_insertion_point(class_scope:StackTopoChange.StackLink)
    ))
  ,

  LinkPortMap = _reflection.GeneratedProtocolMessageType('LinkPortMap', (_message.Message,), dict(
    DESCRIPTOR = _STACKTOPOCHANGE_LINKPORTMAP,
    __module__ = 'forch.proto.faucet_event_pb2'
    # @@protoc_insertion_point(class_scope:StackTopoChange.LinkPortMap)
    ))
  ,

  StackDp = _reflection.GeneratedProtocolMessageType('StackDp', (_message.Message,), dict(
    DESCRIPTOR = _STACKTOPOCHANGE_STACKDP,
    __module__ = 'forch.proto.faucet_event_pb2'
    # @@protoc_insertion_point(class_scope:StackTopoChange.StackDp)
    ))
  ,
  DESCRIPTOR = _STACKTOPOCHANGE,
  __module__ = 'forch.proto.faucet_event_pb2'
  # @@protoc_insertion_point(class_scope:StackTopoChange)
  ))
_sym_db.RegisterMessage(StackTopoChange)
_sym_db.RegisterMessage(StackTopoChange.DpsEntry)
_sym_db.RegisterMessage(StackTopoChange.StackGraph)
_sym_db.RegisterMessage(StackTopoChange.NetworkGraph)
_sym_db.RegisterMessage(StackTopoChange.StackNode)
_sym_db.RegisterMessage(StackTopoChange.StackLink)
_sym_db.RegisterMessage(StackTopoChange.LinkPortMap)
_sym_db.RegisterMessage(StackTopoChange.StackDp)


_STACKTOPOCHANGE_DPSENTRY.has_options = True
_STACKTOPOCHANGE_DPSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
