import socket

HOST = ''
PORT = 9000

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(HOST, PORT)
    print "The server is ready to receive"

    while 1:
        message, clientAddress = server_socket.recvfrom(1000)
        message = message.lower()
        if message == "u":
            file = open("/proc/uptime", "rb")
            data = file.readline()
            server_socket.sendto(data, clientAddress)
        if message == "l":
            file = open("/proc/loadavg", "rb")
            data = file.readline()
            server_socket.sendto(data,clientAddress)


if __name__ == "__main__":
    main()