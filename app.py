from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    socketio.emit('response', f"You've joined the '{room}' room.")

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    leave_room(room)
    socketio.emit('response', f"You've left the '{room}' room.")

@socketio.on('message')
def handle_message(data):
    sender_name = data['sender']
    room = data['room']
    message = data['message']
    print(f"{sender_name} in '{room}' says: {message}")
    socketio.emit('response', f"{sender_name} says: {message}", room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
