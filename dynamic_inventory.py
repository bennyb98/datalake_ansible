#!/usr/bin/env python

import json
import os
import sys
from openstack import connection
from openstack import utils

# Create connection to OpenStack
conn = connection.Connection(
    auth_url=os.environ['OS_AUTH_URL'],
    username=os.environ['OS_USERNAME'],
    password=os.environ['OS_PASSWORD'],
    user_domain_name=os.environ['OS_USER_DOMAIN_NAME'],
    project_domain_id=os.environ['OS_PROJECT_DOMAIN_ID'],
    verify='/home/centos/ansible_material/adacloud.ca.chain'
)

# Get the IP of the "generated VM"
vm_ip = None
for server in conn.compute.servers():
    if server.name == 'my_vm':  # replace with your generated VM name
        vm_ip = server.access_ipv4

# Create inventory
inventory = {
    'virtualmachines': {
        'hosts': {
            'generated_vm': {
                'ansible_host': vm_ip,
                'ansible_user': 'centos',
                'ansible_ssh_private_key_file': '/home/centos/.ssh/vm2key.pem',
                'ansible_python_interpreter': '/usr/bin/python3'
            }
        }
    }
}

print(json.dumps(inventory))

