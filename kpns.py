
from socket import *
from struct import *
import time

print ("kpns client-gw simulator")

Host = '10.1.14.46'
Port = 8100
Addr = (Host, Port)

def process():
	s = socket(AF_INET, SOCK_STREAM)
	s.connect(Addr)

	data = pack('BBHLLL', 1, 0, 0, 0, 0, 0)

	s.send(data)

	while True:
		time.sleep(1)
	#s.close()

if __name__ == "__main__":
	process()

