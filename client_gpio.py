import socket
import RPi.GPIO as GPIO
import SimpleMFRC522
from datetime import datetime
from time import sleep

def get_time(): #get current time and date 
	now = datetime.now()
	now_str = datetime.strftime(now, "%Y.%m.%d %H:%M:%S") 
	return now_str
def read_rfid(): # read rfid tag 
	reader = SimpleMFRC522.SimpleMFRC522() 
	id, text = reader.read()
	return text

sock = socket.socket()
sock.connect(('192.168.1.187',9090))

try:
	while(True):
		
		id = str(id)
		date_for_sent_by_socket_to_server = get_time()+" "+read_rfid() 
		sock.send(date_for_sent_by_socket_to_server.encode('utf-8'))
		data = sock.recv(1024)
		print(data.decode())
		sleep(1)
finally:
	GPIO.cleanup()
	sock.close()
	print("Exit")
	exit()

