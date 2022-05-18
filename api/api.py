import time
from flask import Flask
from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse

app = Flask(__name__, static_folder="web-page/public")


# @app.route("/")
# def home():
#     return send_from_directory(app.static_folder, "index.html")


@app.route("/time")
def currentTime():
    return {"time": time.time()}


if __name__ == "__main__":
    app.run(debug=True)
