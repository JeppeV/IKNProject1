import sys
import socket
from lib import Lib

HOST = ''
PORT = 9000
BUFSIZE = 1000

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("Server awaiting incoming connection...")

    while 1:
        connection_socket, address = server_socket.accept()
        print("Connection with client established")
        file_name = connection_socket.recv(BUFSIZE)
        file_size = Lib.check_File_Exists(file_name)

        if file_size != 0:
            Lib.writeTextTCP("OK", connection_socket)
            print("Sending file of size:", file_size)
            send_file(file_name, connection_socket)
        else:
            Lib.writeTextTCP("ERR", connection_socket)
            print("File not found")

        connection_socket.close()

def send_file(file_name, conn):
    file = open(file_name, "rb")
    for piece in read_in_chunks(file):
        conn.sendall(piece)
    file.close()


def read_in_chunks(file_object):
    while True:
        data = file_object.read(BUFSIZE)
        if not data:
            break
        yield data

if __name__ == "__main__":
    main()
