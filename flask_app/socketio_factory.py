from flask_socketio import SocketIO

from flask_app.routes.socketio.tags import create_tag_routes


def create_socketio_server(app):
    socketio = SocketIO(app, cors_allowed_origins="*")

    create_tag_routes(socketio)

    return socketio
