
import uuid
from datetime import datetime


class TaskManager:

    def __init__(self):
        self.tasks = {}

    def create_task(self, function_name):
        task_id = str(uuid.uuid4())

        self.tasks[task_id] = {
            "function": function_name,
            "status": "PENDING",
            "created_at": datetime.now().isoformat()
        }

        return task_id

    def update_status(self, task_id, status):
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = status

    def get_task(self, task_id):
        return self.tasks.get(task_id)


if __name__ == "__main__":
    manager = TaskManager()

    task_id = manager.create_task("multiply")
    print("Task ID:", task_id)

    manager.update_status(task_id, "COMPLETED")

    print("Task Details:", manager.get_task(task_id))
