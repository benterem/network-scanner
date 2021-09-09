#!/usr/bin/env python

from scapy import all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    
    target_clients = []

    for target in answered_list:
        target_clients.append({"mac": target[1].hwsrc, "ip": target[1].psrc})

    print(target_clients)
    return target_clients

def print_results(targets_list):
    print("_________________________________________\n")
    print("IP\t\t\tMAC ADDRESS")
    print("_________________________________________\n")

    for target in targets_list:
        print(f"{target['ip']}\t\t{target['mac']}")
        print("\n") 


targets_list = scan("192.168.1.69/24")
print_results(targets_list)
