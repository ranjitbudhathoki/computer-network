import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("0.0.0.0", 8000)
s.bind(addr)

while True:
    msg, sender = s.recvfrom(4096)
    print(f"Recived data from ${sender}: ${msg}")
    s.sendto(msg.upper(), sender)
    

    

