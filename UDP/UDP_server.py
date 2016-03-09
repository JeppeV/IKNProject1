import socket

HOST = ''
PORT = 9000

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCKET_DGRAM)
    server_socket.bind(HOST, PORT)
    print "The server is ready  to receive"

    while 1:
        message, clientAddress = server_socket.recvfrom(1000)
        message = message.lower()
        if message == "u":
            #send the u file
        if message == "l":
            #send the l file

