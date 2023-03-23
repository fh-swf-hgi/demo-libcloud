# python3 -m pip install apache-libcloud pycryptodome

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

Driver = get_driver(Provider.GCE)
gce = Driver('pyclient@<Project ID>.iam.gserviceaccount.com',
             '<key>.json',
             datacenter='<Zone>',
             project='<Project ID>')

gce.list_nodes()
node = gce.create_node(name="<User ID>-libcloud-vm", image='ubuntu-minimal-2204-jammy-v20230302', size='f1-micro')
gce.list_nodes()
#node.destroy()
#gce.list_nodes()
