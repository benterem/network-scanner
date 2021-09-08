#!/usr/bin/env python

from scapy import all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())
    scapy.ls(scapy.ARP())

scan("192.1.1.1/24")
