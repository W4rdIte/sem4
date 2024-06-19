import requests
from scapy.all import *

# GNS3 API details
gns3_url = "http://localhost:3080/v2"
project_id = "your_project_id"  # Replace with your GNS3 project ID


# Helper functions for GNS3 API interactions
def create_node(name, node_type, x, y):
    url = f"{gns3_url}/projects/{project_id}/nodes"
    data = {"name": name, "node_type": node_type, "x": x, "y": y}
    response = requests.post(url, json=data)
    return response.json()


def create_link(node_a, adapter_a, node_b, adapter_b):
    url = f"{gns3_url}/projects/{project_id}/links"
    data = {
        "nodes": [
            {"node_id": node_a, "adapter_number": adapter_a, "port_number": 0},
            {"node_id": node_b, "adapter_number": adapter_b, "port_number": 0},
        ]
    }
    response = requests.post(url, json=data)
    return response.json()


def send_commands(node_id, commands):
    url = f"{gns3_url}/projects/{project_id}/nodes/{node_id}/console"
    for cmd in commands:
        requests.post(url, json={"command": cmd})


# Create nodes (routers, switches, PCs)
r5 = create_node("R5", "router", 0, 0)
r6 = create_node("R6", "router", 200, 0)
r2 = create_node("R2", "router", 400, 0)
r3 = create_node("R3", "router", 600, 0)
pc1 = create_node("PC1", "vpcs", 0, 200)
pc2 = create_node("PC2", "vpcs", 200, 200)
switch = create_node("Switch", "ethernet_switch", 200, 100)

# Create links between nodes
create_link(r5["node_id"], 0, r6["node_id"], 0)
create_link(r6["node_id"], 1, r2["node_id"], 0)
create_link(r2["node_id"], 1, switch["node_id"], 0)
create_link(r3["node_id"], 0, switch["node_id"], 1)
create_link(pc1["node_id"], 0, switch["node_id"], 2)
create_link(pc2["node_id"], 0, switch["node_id"], 3)

# Configure IP addresses and routing on routers
commands_r5 = [
    "enable",
    "configure terminal",
    "interface FastEthernet0/0",
    "ip address 192.168.0.1 255.255.255.0",
    "no shutdown",
    "exit",
    "ip route 0.0.0.0 0.0.0.0 192.168.3.1",
    "end",
    "write memory",
]
send_commands(r5["node_id"], commands_r5)

commands_r6 = [
    "enable",
    "configure terminal",
    "interface FastEthernet0/0",
    "ip address 192.168.3.1 255.255.255.0",
    "no shutdown",
    "exit",
    "interface FastEthernet0/1",
    "ip address 192.168.4.1 255.255.255.0",
    "no shutdown",
    "exit",
    "end",
    "write memory",
]
send_commands(r6["node_id"], commands_r6)

commands_r2 = [
    "enable",
    "configure terminal",
    "interface FastEthernet0/0",
    "ip address 192.168.4.2 255.255.255.0",
    "no shutdown",
    "exit",
    "interface FastEthernet0/1",
    "ip address 192.168.2.1 255.255.255.0",
    "no shutdown",
    "exit",
    "end",
    "write memory",
]
send_commands(r2["node_id"], commands_r2)

commands_r3 = [
    "enable",
    "configure terminal",
    "interface FastEthernet0/0",
    "ip address 192.168.2.2 255.255.255.0",
    "no shutdown",
    "exit",
    "end",
    "write memory",
]
send_commands(r3["node_id"], commands_r3)

commands_pc1 = ["ip 192.168.1.2 255.255.255.0 192.168.1.1", "save"]
send_commands(pc1["node_id"], commands_pc1)

commands_pc2 = ["ip 192.168.2.3 255.255.255.0 192.168.2.1", "save"]
send_commands(pc2["node_id"], commands_pc2)


# Packet capture and analysis using Scapy
def capture_packets(interface, count):
    packets = sniff(iface=interface, count=count)
    return packets


def analyze_ping(packets):
    for packet in packets:
        if ICMP in packet:
            print(packet.summary())


# Capture packets on PC2's interface
packets = capture_packets("PC2-eth0", 10)
analyze_ping(packets)
