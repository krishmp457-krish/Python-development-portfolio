
import asyncio
import json
import base64

from tasks.serializer import (
    serialize_task,
    deserialize_result
)

HOST = "127.0.0.1"
PORT = 5002


# Function that will execute on the remote node
def multiply(a, b):
    return a * b


async def send_task(func, *args, **kwargs):

    reader, writer = await asyncio.open_connection(
        HOST, PORT
    )

    print("Connected to MeshWeaver Node")

    task_bytes = serialize_task(func, args, kwargs)

    request = {
        "task": base64.b64encode(
            task_bytes
        ).decode()
    }

    writer.write(
        (json.dumps(request) + "\n").encode()
    )

    await writer.drain()

    print("Task sent successfully!")

    response_data = await reader.readline()

    response = json.loads(response_data.decode())

    if response["status"] == "success":

        result_bytes = base64.b64decode(
            response["result"]
        )

        result = deserialize_result(result_bytes)

        print("Remote execution successful!")
        print("Result received from Node B:", result)

    else:
        print("Remote execution failed:", response["message"])

    writer.close()
    await writer.wait_closed()


async def main():
    await send_task(multiply, 20, 20)


if __name__ == "__main__":
    asyncio.run(main())
