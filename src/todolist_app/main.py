import os
from abc import abstractmethod
from uuid import UUID, uuid4
from typing import List, Dict

from attr import dataclass
from bottle import Bottle, TEMPLATE_PATH, template, request, redirect #type: ignore
from dotenv import load_dotenv


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


def start_app(controller: ControllerPort):
    current_dir = os.path.dirname(__file__)
    views_dir = os.path.join(current_dir, 'views')
    TEMPLATE_PATH.insert(0, views_dir)
    app = Bottle()

    @app.route('/')
    def index():
        return template('index')

    @app.route('/todolist', method='POST')
    def create_todolist():
        todolist_name = request.forms.get('todolist-name')
        todolist_id = controller.create_todolist(name=todolist_name)
        redirect(f'/todolist/{todolist_id}')

    @app.route('/todolist/<uuid>')
    def show_todolist(uuid):
        tasks = controller.get_tasks(todolist_uuid=UUID(uuid))
        return template('todolist', uuid=uuid, tasks=tasks)

    @app.route('/todolist/<todolist_uuid>/task', method='POST')
    def create_task(todolist_uuid):
        task_description = request.forms.get('task_description')
        controller.create_task(todolist_uuid=UUID(todolist_uuid), task_description=task_description)
        redirect(f'/todolist/{todolist_uuid}')

    return app

load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")



class ControllerForDemo(ControllerPort):

    def create_todolist(self, name: str) -> UUID:
        todolist_id = uuid4()
        print(f"Nouvelle liste créée : {name}")
        return todolist_id

    def create_task(self, todolist_uuid: UUID, task_description: str) -> UUID:
        task_id = uuid4()
        print(f"Nouvelle tâche créée dans la liste {todolist_uuid} : {task_description}")
        return task_id

    def get_tasks(self, todolist_uuid: UUID) -> List[TaskPresentation]:
        return [TaskPresentation(uuid=uuid4(), name="buy the milk"), TaskPresentation(uuid=uuid4(), name="eat something")]


start_app(controller=ControllerForDemo()).run(host=host, port=port, reloader=True, debug=True)
