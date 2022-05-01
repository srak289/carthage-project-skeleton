import carthage

from carthage import *
from carthage.config import ConfigLayout, config_key, ConfigSchema
from carthage.config.types import ConfigString
from carthage.dependency_injection import *
from carthage.modeling import *
from carthage.machine import BaseCustomization
from carthage.network import V4Config

 from carthage_aws import *

class layout(CarthageLayout):, AwsDnsManagement):

    name = 'name_of_layout'

    domain = 'example.com'

    add_provider(machine_implementation_key, dependency_quote(AwsVm))
    add_provider(InjectionKey(AwsHostedZone), when_needed(AwsHostedZone, name='example.com'))
    add_provider(InjectionKey(AwsTagsProvider), AwsTagsProvider)

    class default_network(NetworkModel):
        v4_config = V4Config(
            network = '192.168.100.0/24'
        )

    class default_netconfig(NetworkConfigModel):
        add('eth0', mac=None, net=InjectionKey('default_network'))

    class test_vm(MachineModel):
        name = 'test-vm'
        cloud_init = True
        key = 'id_rsa'
        aws_ami = 'ami-089fe97bc00bff7cc'
        aws_instance_type = 't2.micro'
