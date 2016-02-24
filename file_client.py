import sys
import socket
from lib import Lib

PORT = 9000
BUFSIZE = 1000

def main(argv):
    servername = argv[0];
    filename = argv[1];
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((servername, PORT))
    client_socket.send(filename)
    data = client_socket.recv(BUFSIZE)

    client_socket.close()
def receiveFile(fileName,  conn):
   print

if __name__ == "__main__":
    main(sys.argv[1:])
