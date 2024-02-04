from flask_socketio import join_room


def create_tag_routes(socketio):
    @socketio.on('join')
    def on_join(data):
        print(f'Joining room {data["room"]}')
        join_room(data['room'])
