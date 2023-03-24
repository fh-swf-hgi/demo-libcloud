# python3 -m pip install apache-libcloud pycryptodome

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

Driver = get_driver(Provider.GCE)
gce = Driver('pyclient@<Project ID>.iam.gserviceaccount.com',
             'pyclient.json',
             datacenter='<Zone>',
             project='<Project ID>')

gce.list_nodes()
node = gce.create_node(<Ihre Parameter hier>)
gce.list_nodes()
#node.destroy()
#gce.list_nodes()
