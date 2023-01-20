# proxy_client.py
import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "localhost"

# port to connect to
port = 12345

# connection to hostname on the port.
client_socket.connect((host, port))

# Send a request to the server
request = "GET / HTTP/1.1\r\n\r\n"
client_socket.sendall(request.encode())

# receive data from the server
response = client_socket.recv(4096).decode()

# print the response
print(response)

# close the client socket
client_socket.close()
