from flask import Flask, jsonify
import keras
from flask import request
# import tensorflow as tf
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = keras.models.load_model("model.keras") 


@app.route("/", methods=["POST"])
def home():
    print("Received request")
    assert request.method == "POST"
    data: list[int] = request.json
    # modelInput = data
    # print(type(data))

    array = np.array(data).reshape((1, 28, 28, 1))
    predictionVector = model.predict(array)[0]
    result = np.argmax( predictionVector)

    return jsonify({"prediction": str( result ), "confidence": str(predictionVector[result])})


app.run("localhost", 8080, debug=True)
