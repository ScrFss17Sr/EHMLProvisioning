from flask import Flask, Response, request
from flask_cors import CORS
from functools import wraps
#from DBConnector import fetchData
import os

port = 9009

app = Flask(__name__)
port = int(os.getenv("PORT", port))
CORS(app)


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/add', methods=['GET'])
@requires_auth
def add():
    return "Added"

@app.route('/sql', methods=['GET'])
@requires_auth
def executeSQL():
    return fetchData()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True)
