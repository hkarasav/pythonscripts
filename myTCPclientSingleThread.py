# SINGLE THREAD CLIENT IN PYTHON 2 (should work in Pyhon 3)
# Opens a TCP socket and sends a message in 16 bytes chunks. The server accepts 16 bytes from the message each time and sends it back
# Speed test in pending

import socket
import sys
import datetime

# Create a TCP/IP socket
# AF_INET means IPv4
# .SOCK_STREAM means TCP connection. .SOCK_DGRAM would mean UDP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('*** Connecting to {} port {}'.format(server_address[0],server_address[1]))
sock.connect(server_address)

try:
    
    # Send data
    message = 'This is the message. Counter: '
    print('--- Sending "{}"'.format(message))
#    for i in range(2000):
#       sock.sendall(message+str(i))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('--- Received "{}"'.format(data))

finally:
    print('--- Closing socket')
    sock.close()
