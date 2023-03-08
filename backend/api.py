import time

from flask import Flask, request, send_from_directory, jsonify, make_response

import json

from flask_cors import CORS

app = Flask(__name__, static_folder="/public")

CORS(app)

@app.route("/hello")
def helloWorld():
    return "Hello world"

@app.route("/time")
def currentTime():
    return {"time": time.time()}

from MultiLabelClassificationModel import MultiLabelClassificationModel

model = MultiLabelClassificationModel()

from langdetect import detect

@app.route("/predictedTopics", methods=["POST"])
def getPredictedTopics():
    json = request.get_json()

    data = {
        'predictedTopics': model.predict(json['text']),
        'mainLanguage': detect(json['text']),
    }

    return make_response(jsonify(data), 200)

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        # debug=True
    )
