import time
import firebase_admin
from firebase_admin import credentials, initialize_app, firestore

from flask import Flask, request, send_from_directory, jsonify
from flask_restful import Api, Resource, reqparse

import json
import nlp
from pprint import pprint

cred = credentials.Certificate("serviceAccountKey.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__, static_folder="/public")


@app.route("/time")
def currentTime():
    return {"time": time.time()}


@app.route("/filteredText", methods=["POST"])
def getFilteredText():
    text = request.get_json()
    print(text)

    return {
        "filteredText": nlp.filterText(text)
    }


@app.route("/tokenizer", methods=["POST"])
def getTokens():
    text = request.get_json()
    print(text)

    return {
        "tokens": nlp.tokenize(text),
    }

    # if request.method == "POST" and request.is_json:
    #     try:
    # data = request.get_json()
    #         print(data)

    #         return {
    #             "status": "success",
    #             "result": "adasda"
    #         }
    #     except:
    #         return jsonify({"status": "error"})

def addProblem(problemData):
    # Used at TagsBox for component <ReactTags/>
    problemData['topics'] = [{
        "id": topic,
        "name": topic
    } for topic in problemData['topics']]

    # Auto-generated id
    # db.collection('rawProblems').add(problemData)

    def getId(url):
        id = ""
        url = url.split('/')
        if "omegaup.com" in url:
            id = f"omegaup-{url[-1]}"
        elif "codeforces.com" in url:
            id = f"codeforces-{url[-2]}{url[-1]}"
        return id

    # Custom id, url is unique :)
    db.collection('rawProblems').document(getId(problemData['url'])).set(problemData)

    print(f" {problemData['title']} added as {getId(problemData['url'])}")


def getAll():
  problems = db.collection('rawProblems').get()
  return [problem.to_dict() for problem in problems]

if __name__ == "__main__":
    app.run(debug=True)
