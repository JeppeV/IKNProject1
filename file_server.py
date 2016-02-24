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
    print "Server awaiting incoming connection..."

    while 1:
        connection_socket, address = server_socket.accept()
        print "Connection with client established"
        file_name = connection_socket.recv(BUFSIZE)
        file_name = file_name.lower()
        file_size = Lib.check_File_Exists(file_name)
        if file_size != 0:
            print "Attempting to send file of size:", file_size
            connection_socket.sendall("OK")
            send_file(file_name, 1, connection_socket)
        else:
            print "File not found"
            connection_socket.sendall("FNF")
        connection_socket.close()




def send_file(file_name,  file_size,  conn):
    file = open(file_name, "rb")
    for piece in read_in_chunks(file):
        conn.sendall(piece)


def read_in_chunks(file_object):
    chunk_size = 1024
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data




    
if __name__ == "__main__":
    main()
