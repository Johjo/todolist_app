import os  # type: ignore
from uuid import UUID

from bottle import TEMPLATE_PATH, Bottle, template, request, redirect  # type: ignore
from todolist_controller.primary_port import TodolistControllerPort


def start_app(controller: TodolistControllerPort) -> Bottle:
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
        todolist = controller.get_todolist(todolist_key=UUID(uuid))
        return template('todolist', todolist=todolist,
                        events=[event for event in controller.get_events(UUID(uuid))])

    @app.route('/todolist/<todolist_uuid>/task', method='POST')
    def create_task(todolist_uuid) -> None:
        task_description = request.forms.getunicode('task_description')
        controller.open_task(todolist_key=UUID(todolist_uuid), title=task_description, description="")
        redirect(f'/todolist/{todolist_uuid}')

    @app.route('/task/<task_uuid>')
    def show_task(task_uuid) -> None:
        task = controller.get_task(task_key=UUID(task_uuid))
        return template('task', task=task, events=[event for event in controller.get_events(UUID(task_uuid))])

    @app.route('/task/<task_uuid>/close', method='POST')
    def close_task(task_uuid) -> None:
        controller.close_task(task_key=UUID(task_uuid))
        return redirect(f"/task/{task_uuid}")

    @app.route('/task/<parent_task_uuid>/subtask', method='POST')
    def create_subtask(parent_task_uuid) -> None:
        task_description = request.forms.getunicode('subtask_description')
        controller.open_sub_task(parent_task_key=UUID(parent_task_uuid), title=task_description, description="")
        redirect(f'/task/{parent_task_uuid}')

    return app
