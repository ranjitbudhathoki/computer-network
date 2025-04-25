import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 8000))
s.listen()

print("Listening on port 8000")

while True: 
    conn, addr = s.accept()
    print(f"New connection from {addr}")
    while True:
        data = conn.recv(10)
        if not data:
            break
        print(f'Received data {data}')
        conn.send(data)
    print(f'Closing connection {conn}')
    conn.close()

