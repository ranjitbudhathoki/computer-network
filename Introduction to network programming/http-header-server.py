import socket
import json
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM);

s.bind(('0.0.0.0', 3000))
s.listen()

while True: 
    con , addr=  s.accept()
    data = con.recv(4096)
    print(data)
    header, body = data.split(b'\r\n\r\n')
    dict = {}
    for hline in header.split(b'\r\n')[1:]:
        k,v = hline.split(b": ")
        dict[k.decode('ascii')] = v.decode('ascii')
    print(dict)
    con.send(b'HTTP/1.1 200 ok\r\n\r\n')
    con.send(json.dumps(dict).encode('ascii'))
    con.close()
     

  