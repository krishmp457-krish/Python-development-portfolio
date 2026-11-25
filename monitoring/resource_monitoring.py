
import psutil
import time


def get_cpu_usage():
    """Get current CPU usage percentage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage


def get_memory_usage():
    """Get current RAM usage information."""
    memory = psutil.virtual_memory()

    return {
        "total": round(memory.total / (1024 ** 3), 2),
        "available": round(memory.available / (1024 ** 3), 2),
        "used": round(memory.used / (1024 ** 3), 2),
        "percentage": memory.percent
    }


def get_system_resources():
    """Collect CPU and RAM information."""
    resources = {
        "cpu_usage": get_cpu_usage(),
        "memory": get_memory_usage()
    }

    return resources


if __name__ == "__main__":
    print("MeshWeaver - System Resource Monitoring")
    print("----------------------------------------")

    resources = get_system_resources()

    print(f"CPU Usage: {resources['cpu_usage']}%")

    print("\nRAM Information:")
    print(f"Total RAM: {resources['memory']['total']} GB")
    print(f"Used RAM: {resources['memory']['used']} GB")
    print(f"Available RAM: {resources['memory']['available']} GB")
    print(f"RAM Usage: {resources['memory']['percentage']}%")
