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
        return [TaskPresentation(key=uuid4(), name="buy the milk", is_opened=True), TaskPresentation(key=uuid4(), name="eat something", is_opened=True)]

    def get_task(self, task_key: UUID) -> Optional[TaskPresentation]:
        return TaskPresentation(key=task_key, name="buy the milk", is_opened=True)

    def close_task(self, task_uuid: UUID) -> None:
        print(f"Tâche {task_uuid} fermée")
