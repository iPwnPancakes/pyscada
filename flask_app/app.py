from dotenv import load_dotenv

from flask_app.factory import create_flask_app
from flask_app.socketio_factory import create_socketio_server

load_dotenv()

app = create_flask_app()  # Automatically ran when using `flask run` command
socketio = create_socketio_server(app)
