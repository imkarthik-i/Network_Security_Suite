#! /bin/bash

# Flush all existing rules, chains, and zero counters
iptables -F
iptables -X
iptables -Z

# Set default policies to ACCEPT for all chains
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT