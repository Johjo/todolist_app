import os
from abc import abstractmethod

from bottle import Bottle, TEMPLATE_PATH, template, request
from dotenv import load_dotenv


class ControllerPort:
    @abstractmethod
    def create_todolist(self, name: str) -> None:
        pass


def start_app(controller: ControllerPort):
    current_dir = os.path.dirname(__file__)
    views_dir = os.path.join(current_dir, 'views')
    TEMPLATE_PATH.insert(0, views_dir)
    app = Bottle()

    # Ajout du chemin `views` à TEMPLATE_PATH

    @app.route('/')
    def index():
        return template('index')

    @app.route('/todolist', method='POST')
    def create_list():
        list_name = request.forms.get('list_name')
        controller.create_todolist(name=list_name)
        return template('index')

    return app

load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")


class ControllerForDemo(ControllerPort):
    def create_todolist(self, name: str) -> None:
        print(f"Nouvelle liste créée : {name}")



start_app(controller=ControllerForDemo()).run(host=host, port=port, reloader=True)
