import os
from bottle import Bottle, TEMPLATE_PATH, template
from dotenv import load_dotenv

def start_app():
    app = Bottle()

    # Ajout du chemin `views` à TEMPLATE_PATH
    CURRENT_DIR = os.path.dirname(__file__)
    VIEWS_DIR = os.path.join(CURRENT_DIR, 'views')
    TEMPLATE_PATH.insert(0, VIEWS_DIR)


    @app.route('/')
    def index():
        return template('index')

    return app

load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")


app =start_app()
app.run(host=host, port=port)

