import time
from flask import Flask, request, send_from_directory, jsonify
from flask_restful import Api, Resource, reqparse

import json
import nlp
from pprint import pprint

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


if __name__ == "__main__":
    app.run(debug=True)
