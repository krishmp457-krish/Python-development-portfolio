
import cloudpickle


def serialize_task(func, args, kwargs):
    """Convert a function and its arguments into bytes."""
    task_data = (func, args, kwargs)
    return cloudpickle.dumps(task_data)


def deserialize_task(data):
    """Convert bytes back into a function and arguments."""
    return cloudpickle.loads(data)


def serialize_result(result):
    """Convert execution result into bytes."""
    return cloudpickle.dumps(result)


def deserialize_result(data):
    """Convert bytes back into the original result."""
    return cloudpickle.loads(data)
