import sys
import socket
import re


PORT = 9000
BUFSIZE = 1000

def main(argv):
    servername = argv[0];
    file_path = argv[1];
    print file_path
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((servername, PORT))
    receiveFile(file_path, client_socket)

    client_socket.close()
def receiveFile(file_path,  conn):
    l = re.split('[/]+', file_path)
    file_name = l[len(l) - 1]
    file = open(file_name,"wb")
    conn.send(file_path)
    while True:
        data = conn.recv(BUFSIZE)
        if not data:
            break
        file.write(data)


if __name__ == "__main__":
    main(sys.argv[1:])
