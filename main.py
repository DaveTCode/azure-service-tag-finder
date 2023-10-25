import argparse
import json
import ipaddress
import subprocess

parser = argparse.ArgumentParser("Find Service Tag for IP")
parser.add_argument("region", help="The Azure region.", type=str)
parser.add_argument("ip", help="The IP address to check against.", type=str)
args = parser.parse_args()

servicetag_command = subprocess.run(['az','network','list-service-tags', '--location', args.region], capture_output=True)
service_tags = json.loads(servicetag_command.stdout)

for tag in service_tags["values"]:
  for address_prefix in tag["properties"]["addressPrefixes"]:
    if ipaddress.ip_address(args.ip) in ipaddress.ip_network(address_prefix):
      print("{}: {}".format(tag["name"], ipaddress.ip_network(address_prefix)))
