#!/usr/bin/env python

from scapy import all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_req_broadcast, timeout=1)
    print(answered.summary())
    

scan("192.168.1.69/24")
