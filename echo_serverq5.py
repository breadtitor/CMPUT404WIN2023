import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = ""  # Bind to all available interfaces
port = 12345  # Choose a non-privileged port
s.bind((host, port))

# Listen for incoming connections
s.listen()
print("Echo server listening on {}:{}".format(host, port))

while True:
    # Wait for a client to connect
    conn, addr = s.accept()
    print("Client connected from {}:{}".format(addr[0], addr[1]))
    while True:
        try:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            # Print the received data
            print("Received data:", data.decode())
            # Send the received data back to the client
            conn.sendall(data)
        except:
            break
    # Close the client's connection
    conn.close()
    print("Client disconnected")

# Close the server socket
s.close()
