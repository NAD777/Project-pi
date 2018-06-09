import socket
sock = socket.socket()
sock.connect(('192.168.43.187',9090))
sock.send("Hello world")
data = sock.recv(1024)
sock.close()

print(data)