from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from 

app = Flask(__name__, static_folder='web-page/public')


@app.route("/")
def home():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run(debug=True)


api.add_resource(HelloApiHandler, '/flask/hello')