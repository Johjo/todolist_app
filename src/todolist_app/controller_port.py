from abc import abstractmethod
from typing import List, Optional
from uuid import UUID

from attr import dataclass


@dataclass
class TaskPresentation:
    uuid:  UUID
    name: str


class ControllerPort:
    @abstractmethod
    def create_todolist(self, name: str) -> UUID:
        pass

    @abstractmethod
    def create_task(self, todolist_uuid: UUID, task_description: str) -> UUID:
        pass

    @abstractmethod
    def get_tasks(self, todolist_uuid: UUID) -> List[TaskPresentation]:
        pass

    @abstractmethod
    def get_task(self, todolist_uuid: UUID, task_uuid: UUID) -> Optional[TaskPresentation]:
        pass

    @abstractmethod
    def close_task(self, todolist_uuid: UUID, task_uuid: UUID) -> None:
        pass
