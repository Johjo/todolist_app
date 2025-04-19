import os

from bottle import Bottle, TEMPLATE_PATH, template, request, redirect, response  # type: ignore
from dotenv import load_dotenv
from todolist_controller.usage import create_todolist_controller

from todolist_app.primary.app import start_app

load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")

start_app(controller=create_todolist_controller()).run(host=host, port=port, reloader=True, debug=True)
