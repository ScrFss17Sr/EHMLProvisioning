from flask import Flask
import os

app = Flask(__name__)
port = int(os.getenv("PORT", 9005))


@app.route('/', methods=['GET', 'POST'])
def service():
    return "Welcome in Heidelberg"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True)