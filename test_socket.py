from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/echo')
def echo_socket(ws):
    import time
    print 'ws:', ws.
    while not ws.closed:
        counter = 1
        while 1:
            message = ws.receive()
            print 'receive:', message
            if message:
                ws.send('{} {}'.format(counter, message[::-1]))
            else:
                ws.send('counter: {}'.format(counter))
            counter += 1
            time.sleep(1)



@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()