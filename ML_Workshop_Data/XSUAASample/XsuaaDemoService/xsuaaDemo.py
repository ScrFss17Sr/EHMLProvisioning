from flask import Flask, Response, request
from functools import wraps
from VerifyJWTToken import validateJWTToken
import os


app = Flask(__name__)
port = int(os.getenv("PORT", 9009))

@app.route('/', methods=['GET', 'POST'])
def service():
    return "This route is not protected by the XSUAA Service"


@app.route('/protected')
def secret_page():
    print('Validate')
    if validateJWTToken(encoded=getToken(request)) == True:
        return "Now your data and application is secure."
    else:
        return "You are not authorised to see the secret."

def getToken(request = None):
    if request == None:
        return ''

    print('Request Header: ')
    print(request.headers)

    rf = request.headers
    #print('Headers: ', rf['Authorization'])
    return rf['Authorization']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True)
