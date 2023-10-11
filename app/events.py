from flask_socketio import emit

from .extensions import socketio

@socketio.on("connect")
def handle_connect():
    print("Client Connected")

@socketio.on("user_join")
def handle_user_join(name):
    print(f"User {name} joined")

@socketio.on("new_message")
def handle_new_messagen(message):
    print(f"new message is {message}")
    emit("chat", {"message": message}, broadcast=True)