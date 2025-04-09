import os
from bottle import Bottle, TEMPLATE_PATH, template

app = Bottle()

# Ajout du chemin `views` à TEMPLATE_PATH
CURRENT_DIR = os.path.dirname(__file__)
VIEWS_DIR = os.path.join(CURRENT_DIR, 'views')
TEMPLATE_PATH.insert(0, VIEWS_DIR)

host = os.getenv("HOST")
port = os.getenv("PORT")

@app.route('/')
def index():
    return template('index')

app.run(host=host, port=port)

