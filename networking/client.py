
import socket


def start_client():

    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:
        client.connect(("127.0.0.1", 5000))

        print("Connected to MeshWeaver Server!")

        client.sendall(
            "Hello MeshWeaver Server!".encode()
        )

        response = client.recv(1024).decode()

        print("Server response:", response)

    except ConnectionRefusedError:
        print("Server is not running!")

    finally:
        client.close()


if __name__ == "__main__":
    start_client()
