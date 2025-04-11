import os

from bottle import Bottle, TEMPLATE_PATH, template, request, redirect, response #type: ignore
from dotenv import load_dotenv

from todolist_app.primary.app import start_app
from todolist_app.secondary.controller_for_demo import TodolistControllerForDemo

load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")

start_app(controller=TodolistControllerForDemo()).run(host=host, port=port, reloader=True, debug=True)
