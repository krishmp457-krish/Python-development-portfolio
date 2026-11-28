
import socket
import socket
import threading

SERVER_READY = threading.Event()

def start_server():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    try:
        server.bind(("127.0.0.1", 5000))
        server.listen(1)
        SERVER_READY.set()

        print("MeshWeaver Server Started")
        print("Waiting for client...")

        client, address = server.accept()

        print("Client connected:", address)

        message = client.recv(1024).decode()
        print("Received:", message)

        client.sendall(
            "Hello from MeshWeaver!".encode()
        )

        client.close()

    finally:
        server.close()


if __name__ == "__main__":
    start_server()
