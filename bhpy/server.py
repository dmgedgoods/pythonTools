import socket

s = socket.socket()
print("Socket created")

port = 6969

s.bind(("", port))
print("socket bound to port %s" % (port))

s.listen(5)
print("Listening")

while True:
    c, addr = s.accept()
    print("Connection from: ", addr)

    c.close()
