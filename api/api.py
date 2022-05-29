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
from keras.utils.np_utils import to_categorical
import matplotlib.pyplot as plt

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


def sortFile():
    embeddingsFile = open("/home/uriel/CUCEI/Word2VecEnglish.txt", "r")
    wordsFile = open("Word2VectSortedWords.txt", "a")
    linesFile = open("Word2VectSorted", "a")
    embeddingsList = []
    embeddingsWords = []

    for line in embeddingsFile:
        embeddingsList.append(line)
        features = line.split()
        word = features[0]
        embeddingsWords.append(word)

    embeddingsFile.close()
    embeddingsList.sort()
    embeddingsWords.sort()

    for line in embeddingsList:
        linesFile.write(line)

    for word in embeddingsWords:
        wordsFile.write(word)

    wordsFile.close()
    linesFile.close()


class Model:
    reverseTopicMap = {}
    model = Sequential()
    tokenizer = Tokenizer(num_words=5000)
    maxLen = 100

    def train(self, type):
        pprint("Starting model training...")
        pprint("Model type: " + type)
        # Fetch training samples from database
        allProblems = getAll()
        X = []

        # Filter text and create input vectors
        for problemData in allProblems:
            description = problemData["history"]
            description = nlp.filterText(description)
            X.append(description)

        Y = []
        topicMap = {}

        # Compress topics and create output vector
        for problemData in allProblems:
            targetTopic = problemData["topics"][0]["id"]

            if targetTopic not in topicMap:
                topicMap[targetTopic] = len(topicMap)
                self.reverseTopicMap[topicMap[targetTopic]] = targetTopic

            Y.append(topicMap[targetTopic])

        # Split data such that test samples are 20% of the total samples
        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, test_size=0.20)

        # Fix dimensiones so that output matches the number of classses
        Y_train = to_categorical(Y_train, num_classes=len(topicMap))
        Y_test = to_categorical(Y_test, num_classes=len(topicMap))

        # Expand vocabulary
        self.tokenizer.fit_on_texts(X_train)

        # Compress string inputs to numbers inputs
        X_train = self.tokenizer.texts_to_sequences(X_train)
        X_test = self.tokenizer.texts_to_sequences(X_test)

        # Crop out any words that exceed maxLen
        X_train = pad_sequences(X_train, padding='post', maxlen=self.maxLen)
        X_test = pad_sequences(X_test, padding='post', maxlen=self.maxLen)

        # TODO: Find a place to store Word2Vect and use it here
        embeddings = dict()
        embeddingsFile = open("/home/uriel/CUCEI/Word2VecEnglish.txt", "r")
        it = 0

        # Create embeddings dictionary. i.e every word is a vector
        for line in embeddingsFile:
            if (it == 1000):
                break

            it += 1
            features = line.split()
            word = features[0]
            vector = asarray(features[1:], dtype='float32')
            embeddings[word] = vector
        pprint("wtf")
        embeddingsFile.close()
        # TODO: Not sure about this number
        vocabSize = 10000
        embeddingMatrix = np.zeros((vocabSize, 300))

        # Populate embedding matrix. i.e every index is a vector
        for word, index in self.tokenizer.word_index.items():
            embeddingVector = embeddings.get(word)

            if embeddingVector is not None:
                embeddingMatrix[index] = embeddingVector

        # Train neural network
        embeddingLayer = Embedding(vocabSize, 300, weights=[
                                   embeddingMatrix], input_length=self.maxLen, trainable=False)
        self.model.add(embeddingLayer)

        if type == "CNN":
            self.model.add(Conv1D(30, 2, activation='relu'))
            self.model.add(GlobalMaxPooling1D())
        elif type == "LSTM":
            self.model.add(LSTM(200, dropout=0.2, recurrent_dropout=0.2))
        elif type == "DNN":
            self.model.add(Flatten())

        self.model.add(Dense(len(topicMap), activation='softmax'))
        self.model.compile(optimizer='adam',
                           loss='categorical_crossentropy', metrics=['acc'])
        history = self.model.fit(X_train, Y_train, batch_size=8,
                                 epochs=30, verbose=1, validation_split=0.2)
        score = self.model.evaluate(X_test, Y_test, verbose=1)
        print("Test Loss:", score[0])
        print("Test Accuracy:", score[1])

        # Plot cost vs accuracy graphs
        plt.figure(figsize=(12, 5))
        plt.ylim(-0.1, 1.1)
        plt.plot(history.history['acc'])
        plt.plot(history.history['val_acc'])
        plt.title("Model: " + type)
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['Train', 'Validation'])
        plt.show()


# Use DNN, CNN or LSTM to change model
model = Model()
# model.train("DNN")


def instantiateQuery(text):
    text = [nlp.filterText(text)]
    pprint(text)
    model.tokenizer.fit_on_texts(text)
    text = model.tokenizer.texts_to_sequences(text)
    text = pad_sequences(text, padding='post', maxlen=model.maxLen)
    return text


@ app.route("/predictedTopics", methods=["POST"])
def getPredictedTopics():
    text = request.get_json()
    # Compress strings to numbers
    X_test = instantiateQuery(text)
    Y_predictions = model.model.predict(X_test)
    pprint(Y_predictions)
    pprint(model.reverseTopicMap)
    indices = []

    for i in range(len(Y_predictions[0])):
        # Only consider predictions that are good enough
        if Y_predictions[0][i] >= 0.30:
            indices.append(i)

    def customKey(i):
        return Y_predictions[0][i]

    indices.sort(key=customKey)
    predictedTopics = []

    for i in indices:
        predictedTopics.append(model.reverseTopicMap[i])

    return {"predictedTopics": predictedTopics}


@ app.route("/tokenizer", methods=["POST"])
def getTokens():
    text = request.get_json()
    print(text)

    return {"tokens": nlp.tokenize(text)}


@ app.route("/tfIdf", methods=["POST"])
def getTfIdf():
    texts = request.get_json()
    print(texts)

    return {"tfIdf": nlp.tfIdf(texts)}


@ app.route("/topics")
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
    sortFile()
    app.run(debug=True)
