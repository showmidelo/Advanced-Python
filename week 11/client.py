import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234

soc.bind(('127.0.0.1', port))

soc.listen()

while True:
    client, address = soc.accept()
    print(type(client), address)
    client.sendall(b'Hello!\n')
    client.close()