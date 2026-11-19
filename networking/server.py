
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))
server.listen(1)

print("MeshWeaver Server Started")
print("Waiting for client...")

client, address = server.accept()

print("Client connected:", address)

message = client.recv(1024).decode()
print("Received:", message)

client.sendall("Hello from MeshWeaver!".encode())

client.close()
server.close()
