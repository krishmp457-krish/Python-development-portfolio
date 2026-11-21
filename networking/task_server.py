
import asyncio
import json
import base64

from tasks.serializer import (
    deserialize_task,
    serialize_result
)

HOST = "127.0.0.1"
PORT = 5002


async def handle_client(reader, writer):
    address = writer.get_extra_info("peername")
    print(f"Connected to Node: {address}")

    try:
        data = await reader.readline()

        request = json.loads(data.decode())

        task_bytes = base64.b64decode(request["task"])

        func, args, kwargs = deserialize_task(task_bytes)

        print(f"Executing function: {func.__name__}")

        # Run synchronous Python function without blocking
        # the asyncio event loop.
        result = await asyncio.to_thread(
            func, *args, **kwargs
        )

        result_bytes = serialize_result(result)

        response = {
            "status": "success",
            "result": base64.b64encode(
                result_bytes
            ).decode()
        }

        print(f"Task completed. Result: {result}")

    except Exception as e:
        print("Task execution error:", e)

        response = {
            "status": "error",
            "message": str(e)
        }

    try:
        writer.write(
            (json.dumps(response) + "\n").encode()
        )
        await writer.drain()

    finally:
        writer.close()
        await writer.wait_closed()


async def start_server():
    server = await asyncio.start_server(
        handle_client, HOST, PORT
    )

    print(
        f"MeshWeaver Task Server running on {HOST}:{PORT}"
    )

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(start_server())
