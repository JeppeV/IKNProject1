import sys
import socket
import re


PORT = 9000
BUFSIZE = 1000

def main(argv):
    servername = argv[0]
    file_path = argv[1]
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((servername, PORT))
    client_socket.send(file_path)
    receiveFile(file_path, client_socket)
    client_socket.close()

def receiveFile(file_path,  conn):
    l = re.split('[/]+', file_path)
    file_name = l[len(l) - 1]
    file = open(file_name,"wb")
    while True:
        data = conn.recv(BUFSIZE)
        if not data:
            break
        file.write(data)
    file.close()


if __name__ == "__main__":
    main(sys.argv[1:])
