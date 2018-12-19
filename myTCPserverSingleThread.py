# SINGLE THREAD SERVER IN PYTHON 2 (should work in PYTHON 3 as well)
# Opens a TCP socket and sends a message in 16 bytes chunks and then sends it back to the client
# Speed test is pending

import socket
import sys

# Create a TCP/IP socket
# AF_INET means IPv4
# .SOCK_STREAM means TCP connection. .SOCK_DGRAM would mean UDP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port. 0.0.0.0 means accept from any IP
server_address = ('0.0.0.0', 10000)
print('+++ Starting up on {} port {}'.format(server_address[0],server_address[1]))
sock.bind(server_address)

# Listen for only '1' incoming connection
sock.listen(1)

while True:
    print('*** Wait for a connection')
    connection, client_address = sock.accept()

    try:
        print('--- Connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            # recv(16) is a 'blocking' function. That means that the program execution freezes at this point unless data is received
            data = connection.recv(16)
            print('--- Received "{}"'.format(data))
            if data:
                print('--- Sending data back to the client')
                connection.sendall(data)
            else:
                print('--- No more data from', client_address)
                print('----------------------------------------------')
                break
            
    finally:
        # Clean up the connection. If the connection is not explicitly closed then the Python garbage collector closes it.
        connection.close()
