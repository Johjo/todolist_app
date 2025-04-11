from typing import List, Optional
from uuid import UUID, uuid4

from todolist_app.controller_port import ControllerPort, TaskPresentation


class ControllerForDemo(ControllerPort):

    def create_todolist(self) -> UUID:
        todolist_id = uuid4()
        print(f"Nouvelle liste créée : {todolist_id}")
        return todolist_id

    def create_task(self, todolist_uuid: UUID, task_description: str) -> UUID:
        task_id = uuid4()
        print(f"Nouvelle tâche créée dans la liste {todolist_uuid} : {task_description}")
        return task_id

    def get_tasks(self, todolist_uuid: UUID) -> List[TaskPresentation]:
        return [TaskPresentation(uuid=uuid4(), name="buy the milk"), TaskPresentation(uuid=uuid4(), name="eat something")]

    def get_task(self, todolist_uuid: UUID, task_uuid: UUID) -> Optional[TaskPresentation]:
        return TaskPresentation(uuid=task_uuid, name="buy the milk")

    def close_task(self, todolist_uuid: UUID, task_uuid: UUID) -> None:
        print(f"Tâche {task_uuid} fermée dans la liste {todolist_uuid}")
