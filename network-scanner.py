#!/usr/bin/env python

from scapy import all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target_ip", dest="target_ip", help="Target IP for which to find its MAC address")
    parser.add_option("-m", "--mask", dest="mask", help="Network mask for IP")
    (options, arguments) = parser.parse_args()
    
    if not options.target_ip:
        parser.error("[-] Please specify an IP address, use --help for more info")
    if not options.mask:
        return options.target_ip
    
    return options.target_ip + "/" + options.mask


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    
    target_clients = []

    for target in answered_list:
        target_clients.append({"mac": target[1].hwsrc, "ip": target[1].psrc})

    return target_clients

def print_results(targets_list):
    print("_________________________________________\n")
    print("IP\t\t\tMAC ADDRESS")
    print("_________________________________________\n")

    for target in targets_list:
        print(f"{target['ip']}\t\t{target['mac']}")
        print("\n") 

target_ip = get_arguments()
targets_list = scan(target_ip)
print_results(targets_list)
