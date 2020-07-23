import sys
import socket
import itertools

args = sys.argv

with socket.socket() as client_socket:
    hostname = args[1]
    port = int(args[2])
    address = (hostname, port)
    client_socket.connect(address)
    chr = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(1,37):
        ok = True
        for j in itertools.product(chr, repeat = i):
            s = ''.join(j)
            s1 = s
            data = s.encode()
            client_socket.send(data)
            response = client_socket.recv(1024)
            response = response.decode()
            if(response == "Connection success!"):
                print(s1)
                ok = False
                break
        if not ok:
            break
