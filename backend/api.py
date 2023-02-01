import time
import firebase_admin
from firebase_admin import credentials, initialize_app, firestore

from flask import Flask, request, send_from_directory, jsonify
from flask_restful import Api, Resource, reqparse

import json
from topicsStandardization import codeforcesToOmegaup
from pprint import pprint

import dummy

cred = credentials.Certificate("serviceAccountKey.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__, static_folder="/public")

@app.route("/time")
def currentTime():
    return {"time": time.time()}


from MultiLabelClassificationModel import MultiLabelClassificationModel

model = MultiLabelClassificationModel()

@app.route("/predictedTopics", methods=["POST"])
def getPredictedTopics():
    text = request.get_json()
    # print(text)
    return {"predictedTopics": model.predict(text)}


# @app.route("/topics")
# def getTopics():
#     return {"topics": codeforcesToOmegaup.keys()}


def addProblem(problemData):
    def getProblemId(url):
        """
        Returns problem id used in firebase
        """
        id = ""
        url = url.split("/")
        if "omegaup.com" in url:
            id = f"omegaup-{url[-1]}"
        elif "codeforces.com" in url:
            id = f"codeforces-{url[-2]}{url[-1]}"
        return id

    # Custom id, url is unique :)
    id = utils.getProblemId(problemData["url"])
    db.collection("rawProblems").document(id).set(problemData)

    print(f" {problemData['title']} added as {id}")


if __name__ == "__main__":
    app.run(debug=True)
