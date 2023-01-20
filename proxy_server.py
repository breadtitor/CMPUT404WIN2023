# proxy_server.py
import socket
import os

def handle_client(client_socket):
    # get request from client
    request = client_socket.recv(4096)

    # forward request to google.com
    google_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    google_socket.connect(("www.google.com", 80))
    google_socket.sendall(request)

    # receive response from google.com
    response = google_socket.recv(4096)

    # send response back to client
    client_socket.sendall(response)

    # close client and google sockets
    client_socket.close()
    google_socket.close()

def start_server():
    # create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to a specific address and port
    server_socket.bind(("0.0.0.0", 12345))

    # become a server socket
    server_socket.listen(5)

    while True:
        # establish a connection
        (client_socket, client_address) = server_socket.accept()
        pid = os.fork()
        if pid == 0:
            server_socket.close()
            handle_client(client_socket)
            exit()
        else:
            client_socket.close()

if __name__ == "__main__":
    start_server()
