from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import tensorflow as tf
from tensorflow import keras


app = Flask(__name__)


@app.route('/predict/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = '../LoanPredictionModel/my_model'
    # model = p.load(open(modelfile, 'rb'))
    print(modelfile)
    model = tf.keras.models.load_model(modelfile)
    app.run(debug=True, host='0.0.0.0') 