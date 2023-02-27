import time

from flask import Flask, request, send_from_directory, jsonify, make_response
from flask_restful import Api, Resource, reqparse

import json
from topicsStandardization import codeforcesToOmegaup

import dummy

from flask_cors import CORS

app = Flask(__name__, static_folder="/public")
# app = Flask(__name__)
CORS(app)

@app.route("/hello")
def helloWorld():
    return "Hello world"

@app.route("/time")
def currentTime():
    return {"time": time.time()}


from MultiLabelClassificationModel import MultiLabelClassificationModel

model = MultiLabelClassificationModel()

# @app.route("/predictedTopics", methods=["OPTIONS"])
# def getPredictedTopicsOptions():
#     return make_response({}, 200)

@app.route("/predictedTopics", methods=["POST"])
def getPredictedTopics():
    json = request.get_json()
    data = {
        'predictedTopics': model.predict(json['text'])
    }
    return make_response(jsonify(data), 200)

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
    )
