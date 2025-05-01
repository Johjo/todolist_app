import os

from bottle import Bottle, TEMPLATE_PATH, template, request, redirect, response  # type: ignore
from dotenv import load_dotenv
from todolist_controller.usage import create_todolist_controller

from todolist_app.primary.app import start_app

load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

start_app(controller=create_todolist_controller(db_name=db_name, db_user=db_user, db_host=db_host, db_port=db_port,
                                                db_password=db_password)).run(host=host, port=port, reloader=True,
                                                                              debug=True)
