import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print ('connected:', addr)
try:
	while True:
		
		while True:
		    data = conn.recv(1024)
		    if not data:
		        break
		    # conn.send(data.upper())
		    conn.send('You have connected'.encode("utf-8"))
		    print(data.decode())
except KeyboardInterrupt:
	print('Exit')
	conn.close()
	exit()
