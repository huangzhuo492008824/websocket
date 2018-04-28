from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from redisDB import RedisDB

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('client_request')
def test_message(message):
    print 'received:', message
    redis = RedisDB()
    redis.set(key=message.get('socket_id'), val=None)
    import time
    counter = 5
    while counter:
        print 'enter 1:', message.get('socket_id')
        if redis.get(message.get('socket_id')):
            emit('server_push', {'data': 'got it!'})
        else:
            emit('server_push', 'not val')
        time.sleep(1)
        counter -= 1


if __name__ == '__main__':
    socketio.run(app=app, port=9003)
