import os

from bottle import Bottle, TEMPLATE_PATH, template, request, redirect, response #type: ignore
from dotenv import load_dotenv

from src.todolist_app.app import start_app
from src.todolist_app.secondary.controller_for_demo import ControllerForDemo

load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")

start_app(controller=ControllerForDemo()).run(host=host, port=port, reloader=True, debug=True)
