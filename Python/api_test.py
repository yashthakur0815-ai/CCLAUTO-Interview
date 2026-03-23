import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("mask")
args = parser.parse_args()

api = "https://networkcalc.com/api/ip"
class_A = "10.0.0.0"
class_B = "172.16.0.0"
class_C = "192.168.1.0"

mask = args.mask
subnet = class_B  


def api_call():
    url = f"{api}/{subnet}/{mask}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    address = data["address"]

    hosts = address["assignable_hosts"]
    first_ip = address["first_assignable_host"]
    subnet_mask = address["subnet_mask"]
    subnet_bits = address["subnet_bits"]
    cidr = address["cidr_notation"]

    return hosts, first_ip, subnet_mask, subnet_bits, cidr


def assignable_hosts(hosts, cidr):
    print("There are", hosts, "assignable hosts for the", cidr, "subnet")


def first_host(first_ip):
    print("The first address is", first_ip)


def mask_decimal(subnet_mask):
    print("The subnet mask in decimal form is", subnet_mask)


def mask_cidr(subnet_bits):
    print("The subnet mask in cidr notation is", f"/{subnet_bits}")


if __name__ == '__main__':
    hosts, first_ip, subnet_mask, subnet_bits, cidr = api_call()
    assignable_hosts(hosts, cidr)
    first_host(first_ip)
    mask_decimal(subnet_mask)
    mask_cidr(subnet_bits)