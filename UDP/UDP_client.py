import socket
PORT = 9000

def main(argv):
    servername = argv[0]
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    command = raw_input("Enter command (u or l) ")
    client_socket.sendto(command, (servername, PORT))
    output, server_address = client_socket.recvfrom(1000)
    print "You specified the command ", command, " and received: " , output
    client_socket.close()



if __name__ == "__main__":
    main()