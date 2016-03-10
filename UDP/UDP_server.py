import socket

HOST = ''
PORT = 9000

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print("The server is ready to receive")

    while 1:
        message, client_address = server_socket.recvfrom(1000)
        message = message.lower()
        if message == "u":
            file_object = open("/proc/uptime", "rb")
            data = file_object.readline()
        elif message == "l":
            file_object = open("/proc/loadavg", "rb")
            data = file_object.readline()
        else:
            data = "ERR"
        server_socket.sendto(data, client_address)
        if file_object:
            file_object.close()


if __name__ == "__main__":
    main()