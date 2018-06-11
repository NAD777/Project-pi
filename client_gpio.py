import socket
import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

sock = socket.socket()
sock.connect(('192.168.1.187',9090))
try:
	while(True):
		id, text = reader.read()
		id = str(id)
		sock.send(id.encode('utf-8'))
		data = sock.recv(1024)
		print(data.decode())
finally:
	GPIO.cleanup()
	sock.close()
	print("Exit")
	exit()

