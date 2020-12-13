import random

from flask import Flask, send_file
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = '08dec6e9-e497-473b-b48f-5ef1dabdaa79'
socketio = SocketIO(app)

counter = 0

current_target = None
current_users = set()


def generate_new_target():
    global current_target
    current_target = random.randint(1, 10)
    print('Current target = {}'.format(current_target))


@app.route('/')
def index():
    return send_file('./index.html')


@app.route('/counter')
def counter_route():
    global counter
    counter += 1
    return 'Counter {}'.format(counter)


@socketio.on('connect')
def client_connect():
    print('Client connected')


@socketio.on('disconnect')
def client_disconnect():
    print('Client disconnected')


@socketio.on('new user')
def handle_new_user(json):
    print('### Got new user {}'.format(json['name']))
    current_users.add(json['name'])


@socketio.on('submit guess')
def handle_submit_guess(json):
    name = json['name']
    guess = json['guess']
    if guess == current_target:
        print('### User {} correctly guessed {}'.format(name, guess))
        # Let everyone know that we have a correct guess
        emit('correct guess', {'name': name, 'guess': guess}, broadcast=True)
        generate_new_target()
    else:
        print('### User {} incorrectly guessed {}'.format(name, guess))


if __name__ == '__main__':
    generate_new_target()
    socketio.run(app, host='0.0.0.0', port=8080)
