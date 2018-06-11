import socket
import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

sock = socket.socket()
sock.connect(('192.168.43.187',9090))
try:
	sock.send("Hello world".encode("utf-8"))
	data = sock.recv(1024)

print(data.decode())
finally:
	GPIO.cleanup()
	sock.close()

