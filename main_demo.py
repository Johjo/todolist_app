import os

from bottle import Bottle, TEMPLATE_PATH, template, request, redirect, response #type: ignore
from dotenv import load_dotenv


load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")

