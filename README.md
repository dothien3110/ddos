# ddos python example
Use VMware or VirtualBox to create 2 virtual machines (1 for attacker, 1 for victim)<br>
OS can choose Windows Server for victim, Ubuntu for victim<br>
+ In victim: install apache or Nginx (can be tracked by htop, iftop, netstat -ant, tcpdump, wireshark)<br>
+ In attacker : <br>
    pip install scapy requests<br>
    sudo python3 ddos_lab_cli.py<br>
    (bash)

