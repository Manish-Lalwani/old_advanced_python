from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('event1',namespace='/socket')
def test_message(message):
    dict1 = {'data':message['data']}
    emit('response1',)