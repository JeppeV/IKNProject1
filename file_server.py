import sys
import socket
from lib import Lib

HOST = ''
PORT = 9000
BUFSIZE = 1000

def main(argv):
	serversocket = socket.socket(
      socket.AF_INET, socket.SOCK_STREAM)
   #bind the socket to a public host,
   # and a well-known port
   serversocket.bind((socket.gethostname(), 80))
   #become a server socket
   serversocket.listen(5)

def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code
    
if __name__ == "__main__":
   main(sys.argv[1:])
