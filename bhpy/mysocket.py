import socket

address = "127.0.0.1"
port = 6969
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((address, port))

print(s)
