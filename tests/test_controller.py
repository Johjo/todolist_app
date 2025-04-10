from abc import abstractmethod, ABC
from typing import Optional, List
from uuid import UUID, uuid4

from todolist_app.controller_port import ControllerPort, TaskPresentation


class UuidGeneratorPort(ABC):
    @abstractmethod
    def generate_uuid(self):
        pass


class Controller(ControllerPort):
    def __init__(self, uuid_generator : UuidGeneratorPort) -> None:
        self._uuid_generator : UuidGeneratorPort = uuid_generator

    def create_todolist(self) -> UUID:
        return self._uuid_generator.generate_uuid()

    def create_task(self, todolist_uuid: UUID, task_description: str) -> UUID:
        raise NotImplementedError()

    def get_tasks(self, todolist_uuid: UUID) -> List[TaskPresentation]:
        raise NotImplementedError()

    def get_task(self, todolist_uuid: UUID, task_uuid: UUID) -> Optional[TaskPresentation]:
        raise NotImplementedError()

    def close_task(self, todolist_uuid: UUID, task_uuid: UUID) -> None:
        raise NotImplementedError()


class UuidGeneratorForTest(UuidGeneratorPort):
    def __init__(self) -> None:
        self._next : UUID | None = None

    def feed(self, next_uuid: UUID) -> None:
        self._next = next_uuid

    def generate_uuid(self) -> UUID:
        if self._next is None:
            raise Exception("next uuid not fed")

        return self._next


def test_get_created_todolist_uuid_when_create_todolist():
    uuid_generator = UuidGeneratorForTest()
    sut = Controller(uuid_generator)
    expected_todolist_id = uuid4()
    uuid_generator.feed(expected_todolist_id)

    todolist_id = sut.create_todolist(name="my todolist")

    assert todolist_id == expected_todolist_id
