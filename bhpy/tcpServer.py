import socket
import threading

# address and port we are listening on
IP = "0.0.0.0"
PORT = 9001


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))  # pass the IP and PORT from our magic values above
    server.listen(5)  # maximum connection backlog
    print(f"[*] Listening on {IP}:{PORT}")

    while True:
        client, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b"ACK")


if __name__ == "__main__":
    main()
