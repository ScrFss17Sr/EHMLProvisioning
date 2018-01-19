from flask import Flask, Response, request
from functools import wraps
import os


app = Flask(__name__)
port = int(os.getenv("PORT", 9009))

@app.route('/', methods=['GET', 'POST'])
def service():
    return "Welcome in Heidelberg"



def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'eh' and password == 'welcome'

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

@app.route('/protected')
@requires_auth
def secret_page():
    return "This shows a secret."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True)

    #cf map-route approuter-p2000000225trial cfapps.sap.hana.ondemand.com
    # -n approuter-p2000000225trial.cfapps.eu10.hana.ondemand.com

    #cf create-service xsuaa application my-xsuaa -c xs-security.json
