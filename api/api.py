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

from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from api import nlp
import numpy as np
import tensorflow as tf
from numpy import asarray
from pprint import pprint

from numpy import array
from keras_preprocessing.sequence import pad_sequences
from tensorflow.keras import Sequential
from keras.layers.core import Activation, Dropout, Dense
from keras.layers import Flatten, Conv1D, LSTM, GlobalMaxPooling1D
from tensorflow.keras.layers import Embedding

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


def getAll():
    # TODO: Test if works u.u
    rawProblemsRef = db.collection("rawProblems")
    query = rawProblemsRef.limit(300)
    problems = query.stream()
    return [problem.to_dict() for problem in problems]


class Model:
    reverseClassMap = {}
    model = Sequential()
    tokenizer = Tokenizer(num_words=5000)
    maxLen = 100

    def train(self):
        pprint("Starting model training...")
        allProblems = getAll()
        pprint(allProblems[:5])
        X = []

        for problemData in allProblems:
            description = problemData["history"]
            description = nlp.filterText(description)
            X.append(description)

        pprint(X[:5])
        Y = []
        classMap = {}

        for problemData in allProblems:
            targetClass = problemData["topics"][0]["id"]

            if targetClass not in classMap:
                classMap[targetClass] = len(classMap)
                self.reverseClassMap[classMap[targetClass]] = targetClass

            Y.append(classMap[targetClass])

        pprint(Y[:5])
        pprint(classMap)

        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, test_size=0.20)
        Y_train = tf.one_hot(Y_train, depth=len(classMap))
        Y_test = tf.one_hot(Y_test, depth=len(classMap))

        self.tokenizer.fit_on_texts(X_train)
        X_train = self.tokenizer.texts_to_sequences(X_train)
        X_test = self.tokenizer.texts_to_sequences(X_test)

        X_train = pad_sequences(X_train, padding='post', maxlen=self.maxLen)
        X_test = pad_sequences(X_test, padding='post', maxlen=self.maxLen)

        # TODO: Find a place to store Word2Vect and use it here
        embeddings = dict()
        embeddingsFile = open("/home/uriel/CUCEI/Word2VecEnglish.txt", "r")
        it = 0

        for line in embeddingsFile:
            # TODO: Remove this in production
            if it == 100:
                break

            it += 1
            features = line.split()
            word = features[0]
            vector = asarray(features[1:], dtype='float32')
            embeddings[word] = vector

        embeddingsFile.close()
        # TODO: Not sure about this number
        vocabSize = 10000
        embeddingMatrix = np.zeros((vocabSize, 300))

        for word, index in self.tokenizer.word_index.items():
            embeddingVector = embeddings.get(word)

            if embeddingVector is not None:
                embeddingMatrix[index] = embeddingVector

        embeddingLayer = Embedding(vocabSize, 300, weights=[
                                   embeddingMatrix], input_length=self.maxLen, trainable=False)
        self.model.add(embeddingLayer)
        self.model.add(Flatten())
        self.model.add(Dense(len(classMap), activation='sigmoid'))
        self.model.compile(optimizer='adam',
                           loss='binary_crossentropy', metrics=['acc'])
        self.model.fit(X_train, Y_train, batch_size=128,
                       epochs=10, verbose=1, validation_split=0.2)
        score = self.model.evaluate(X_test, Y_test, verbose=1)
        print("Test Loss:", score[0])
        print("Test Accuracy:", score[1])


model = Model()
model.train()


def textToSequences(text):
    text = [text]
    model.tokenizer.fit_on_texts(text)
    text = model.tokenizer.texts_to_sequences(text)
    text = pad_sequences(text, padding='post', maxlen=model.maxLen)
    return text


@app.route("/predictedTopics", methods=["POST"])
def getPredictedTopics():
    text = request.get_json()
    pprint(text)
    X_test = textToSequences(text)
    Y_predictions = model.model.predict(X_test)
    indices = tf.argmax(Y_predictions, axis=1)
    pprint(Y_predictions)
    pprint(model.reverseClassMap)

    return {"predictedTopics": [model.reverseClassMap[int(indices[0])]]}


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


if __name__ == "__main__":
    app.run(debug=True)
