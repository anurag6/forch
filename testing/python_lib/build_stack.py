"""Integration test base class for Forch"""
import time

from test_failscale import FailScaleConfigTest


class SetupBuilder():
    """Test suite for failure modes during scaling"""

    def __init__(self, switches=2, devices=2):
        self.stack_builder = FailScaleConfigTest(switches=switches, devices=devices)

    def build_setup(self):
        self.stack_builder.setUp()
        self.stack_builder.add_faux_devices()

def verify_stack_state(static_state, setup_builder):
    for index in range(200):
        stack_state = setup_builder.stack_builder.get_varz_dump('0.0.0.0:8001', 'dp_root_hop_port')
        print(stack_state)
        time.sleep(1)


if __name__ == '__main__':
    setup_builder = SetupBuilder(switches=13, devices=100)
    setup_builder.build_setup()
    static_state = {
        '{dp_id="0xb1",dp_name="nz-kiwi-t1sw1"}': '0.0',
        '{dp_id="0xb2",dp_name="nz-kiwi-t1sw2"}': '6.0',
        '{dp_id="0x50f",dp_name="nz-kiwi-t2sw1"}': '50.0',
        '{dp_id="0x518",dp_name="nz-kiwi-t2sw10"}': '50.0',
        '{dp_id="0x510",dp_name="nz-kiwi-t2sw2"}': '50.0',
        '{dp_id="0x511",dp_name="nz-kiwi-t2sw3"}': '50.0',
        '{dp_id="0x512",dp_name="nz-kiwi-t2sw4"}': '50.0',
        '{dp_id="0x513",dp_name="nz-kiwi-t2sw5"}': '50.0',
        '{dp_id="0x514",dp_name="nz-kiwi-t2sw6"}': '50.0',
        '{dp_id="0x515",dp_name="nz-kiwi-t2sw7"}': '50.0',
        '{dp_id="0x516",dp_name="nz-kiwi-t2sw8"}': '50.0',
        '{dp_id="0x517",dp_name="nz-kiwi-t2sw9"}': '50.0'
    }
    verify_stack_state(static_state, setup_builder)
