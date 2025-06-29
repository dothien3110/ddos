# ddos python example
Use VMware or VirtualBox to create 2 virtual machines (1 for attacker, 1 for victim)
OS can choose Windows Server for victim, Ubuntu for victim
In victim: install apache or Nginx (can be tracked by htop, iftop, netstat -ant, tcpdump, wireshark)
In attacker : 
pip install scapy requests
sudo python3 ddos_lab_cli.py
(bash)

