import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("0.0.0.0", 3000))

while True:
    data, addr = s.recvfrom(1000)
    s.sendto(data.upper(), addr)