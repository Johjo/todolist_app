from typing import List, Optional
from uuid import UUID, uuid4

from todolist_app.controller_port import ControllerPort, TaskPresentation


class ControllerForDemo(ControllerPort):

    def create_todolist(self) -> UUID:
        todolist_id = uuid4()
        print(f"Nouvelle liste créée : {todolist_id}")
        return todolist_id

    def open_task(self, todolist_uuid: UUID, task_description: str) -> UUID:
        task_id = uuid4()
        print(f"Nouvelle tâche créée dans la liste {todolist_uuid} : {task_description}")
        return task_id

    def get_tasks(self, todolist_uuid: UUID) -> List[TaskPresentation]:
        return [TaskPresentation(uuid=uuid4(), name="buy the milk"), TaskPresentation(uuid=uuid4(), name="eat something")]

    def get_task(self, todolist_id: UUID, task_id: UUID) -> Optional[TaskPresentation]:
        return TaskPresentation(uuid=task_id, name="buy the milk")

    def close_task(self, todolist_id: UUID, task_id: UUID) -> None:
        print(f"Tâche {task_id} fermée dans la liste {todolist_id}")
