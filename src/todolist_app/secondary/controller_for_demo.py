from typing import List, Optional
from uuid import UUID, uuid4

from todolist_controller.primary_port import TodolistControllerPort, TaskPresentation


class TodolistControllerForDemo(TodolistControllerPort):

    def create_todolist(self) -> UUID:
        todolist_id = uuid4()
        print(f"Nouvelle liste créée : {todolist_id}")
        return todolist_id

    def open_task(self, todolist_id: UUID, title: str, description: str) -> UUID:
        task_id = uuid4()
        print(f"Nouvelle tâche créée dans la liste {todolist_id} : {title} - {description}")
        return task_id

    def get_tasks(self, todolist_id: UUID) -> List[TaskPresentation]:
        return [TaskPresentation(uuid=uuid4(), name="buy the milk"), TaskPresentation(uuid=uuid4(), name="eat something")]

    def get_task(self, todolist_key: UUID, task_key: UUID) -> Optional[TaskPresentation]:
        return TaskPresentation(uuid=task_key, name="buy the milk")

    def close_task(self, todolist_uuid: UUID, task_uuid: UUID) -> None:
        print(f"Tâche {task_uuid} fermée dans la liste {todolist_uuid}")
