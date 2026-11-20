
import asyncio

HOST = "127.0.0.1"
PORT = 5001


async def handle_client(reader, writer):
    address = writer.get_extra_info("peername")
    print(f"Connected to: {address}")

    try:
        data = await reader.readline()

        message = data.decode().strip()
        print(f"Received: {message}")

        response = f"Message received by MeshWeaver: {message}\n"

        writer.write(response.encode())
        await writer.drain()

    except Exception as e:
        print("Error:", e)

    finally:
        writer.close()
        await writer.wait_closed()
        print("Client disconnected")


async def start_server():
    server = await asyncio.start_server(
        handle_client, HOST, PORT
    )

    print(f"MeshWeaver Async Server running on {HOST}:{PORT}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(start_server())
