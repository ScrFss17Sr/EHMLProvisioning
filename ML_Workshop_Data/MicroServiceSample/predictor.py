from flask import Flask, request
from ModelBuilder import LinearRegressionModel
import numpy as np
import os

model = LinearRegressionModel()

app = Flask(__name__)
port = int(os.getenv("PORT", 9005))

@app.route('/', methods=['GET', 'POST'])
def service():
    return "Welcome to our prediction Service"

@app.route('/predict/<x>', methods=['GET'])
def prediction(x):
    if request.method == 'GET':
        x = float(x)
        input = np.array([x]).reshape(-1,1)

        res = model.makePrediction(x_data=input)
        return np.array_str(res)
    return ""

if __name__ == '__main__':
    model.trainModel()
    app.run(host='0.0.0.0', port=port, threaded=True)
