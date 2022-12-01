import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234

soc.connect(('127.0.0.1', port))

print(soc.recv(1024))
soc.close() 