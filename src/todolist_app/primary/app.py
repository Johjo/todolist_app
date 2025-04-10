import os
from uuid import UUID

from bottle import TEMPLATE_PATH, Bottle, template, request, redirect #type: ignore

from todolist_app.controller_port import ControllerPort


def start_app(controller: ControllerPort) -> Bottle:
    current_dir = os.path.dirname(__file__)
    views_dir = os.path.join(current_dir, 'views')
    TEMPLATE_PATH.insert(0, views_dir)
    app = Bottle()

    @app.route('/')
    def index() -> None:
        return template('index')

    @app.route('/todolist', method='POST')
    def create_todolist() -> None:
        todolist_id = controller.create_todolist()
        redirect(f'/todolist/{todolist_id}')

    @app.route('/todolist/<uuid>')
    def show_todolist(uuid) -> None:
        tasks = controller.get_tasks(todolist_uuid=UUID(uuid))
        return template('todolist', uuid=uuid, tasks=tasks)

    @app.route('/todolist/<todolist_uuid>/task', method='POST')
    def create_task(todolist_uuid) -> None:
        task_description = request.forms.get('task_description')
        controller.open_task(todolist_uuid=UUID(todolist_uuid), task_description=task_description)
        redirect(f'/todolist/{todolist_uuid}')

    @app.route('/todolist/<todolist_uuid>/task/<task_uuid>')
    def show_task(todolist_uuid, task_uuid) -> None:
        task = controller.get_task(todolist_uuid=UUID(todolist_uuid), task_uuid=UUID(task_uuid))
        return template('task', todolist_uuid=todolist_uuid, task=task)

    return app
