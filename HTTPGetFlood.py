import requests
import threading

target = "http://192.168.56.101"  

def send_request():
    while True:
        try:
            r = requests.get(target)
            print(f"Status: {r.status_code}")
        except:
            pass

for i in range(10): 
    t = threading.Thread(target=send_request)
    t.start()
