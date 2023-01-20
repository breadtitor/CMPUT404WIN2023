import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = "www.google.com"

# Reserve a port for your service.
port = 80

# Connect to host
s.connect((host, port))

# Send a request to the server
s.sendall(b"GET / HTTP/1.1\r\n\r\n")

# Receive data from the server
data = s.recv(1024)

# Close the socket
s.close()

# Print the received data
print(data.decode())
