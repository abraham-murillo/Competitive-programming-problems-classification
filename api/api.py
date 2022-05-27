import time
import firebase_admin
from firebase_admin import credentials, initialize_app, firestore

from flask import Flask, request, send_from_directory, jsonify
from flask_restful import Api, Resource, reqparse

import json
import nlp
import utils
from topicsStandardization import codeforcesToOmegaup
from pprint import pprint

cred = credentials.Certificate("serviceAccountKey.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__, static_folder="/public")


@app.route("/time")
def currentTime():
    return {"time": time.time()}


# @app.route("/filteredText", methods=["POST"])
# def getSomething():
#     if request.method == "POST" and request.is_json:
#         try:
#            # do something
#         except:
#             return {"status": "error"}


@app.route("/filteredText", methods=["POST"])
def getFilteredText():
    text = request.get_json()
    print(text)

    return {"filteredText": nlp.filterText(text)}


@app.route("/tokenizer", methods=["POST"])
def getTokens():
    text = request.get_json()
    print(text)

    return {"tokens": nlp.tokenize(text)}


@app.route("/tfIdf", methods=["POST"])
def getTfIdf():
    texts = request.get_json()
    print(texts)

    return {"tfIdf": nlp.tfIdf(texts)}


@app.route("/topics")
def getTopics():
    return {"topics": utils.topicsForReact(codeforcesToOmegaup.keys())}


def addProblem(problemData):
    problemData["topics"] = utils.topicsForReact(problemData["topics"])

    # Auto-generated id
    # db.collection('rawProblems').add(problemData)

    # Custom id, url is unique :)
    id = utils.getProblemId(problemData["url"])
    db.collection("rawProblems").document(id).set(problemData)

    print(f" {problemData['title']} added as {id}")


def getAll():
    # TODO: Test if works u.u
    rawProblemsRef = db.collection("rawProblems")
    query = rawProblemsRef.limit(5)
    problems = query.stream()
    return [problem.to_dict() for problem in problems]


if __name__ == "__main__":
    app.run(debug=True)
