
import asyncio

HOST = "127.0.0.1"
PORT = 5001


async def send_message(message):

    reader, writer = await asyncio.open_connection(
        HOST, PORT
    )

    print(f"Sending: {message}")

    writer.write((message + "\n").encode())
    await writer.drain()

    response = await reader.readline()

    print("Server response:", response.decode().strip())

    writer.close()
    await writer.wait_closed()


async def main():

    messages = [
        "Hello from Node A",
        "Hello from Node B",
        "Hello from Node C"
    ]

    await asyncio.gather(
        *(send_message(msg) for msg in messages)
    )


if __name__ == "__main__":
    asyncio.run(main())
