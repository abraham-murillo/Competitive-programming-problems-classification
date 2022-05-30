import nlp
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
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


class Model:
    reverseTopicMap = {}
    model = Sequential()
    tokenizer = Tokenizer(num_words=5000)
    maxLen = 100

    def train(self, type, allProblems):
        pprint("Starting model training...")
        pprint("Model type: " + type)
        # Fetch training samples from database
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
            targetTopic = problemData["topics"][0]

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

        # Create dictionary of tokens
        tokenIndex = {}

        for word, index in self.tokenizer.word_index.items():
            tokenIndex[word] = index

        pprint("Creating embeddings matrix...")
        # TODO: Find a place to store Word2Vect and use it here
        embeddingsFile = open("/home/uriel/CUCEI/Word2VecEnglish.txt", "r")
        # TODO: Not sure about this number
        vocabSize = 10000
        embeddingMatrix = np.zeros((vocabSize, 300))

        # Create embeddings matrix. i.e every word is a vector
        for line in embeddingsFile:
            features = line.split()
            token = features[0]

            if token in tokenIndex:
                vector = asarray(features[1:], dtype='float32')
                embeddingMatrix[tokenIndex[token]] = vector

        embeddingsFile.close()

        # Train neural network
        pprint("Training neural network...")
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

        self.plotGraph(history, type)

    def plotGraph(self, history, type):
        plt.figure(figsize=(12, 5))
        plt.ylim(-0.1, 1.1)
        plt.plot(history.history['acc'])
        plt.plot(history.history['val_acc'])
        plt.title("Model: " + type)
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['Train', 'Validation'])
        plt.show()

    def instantiateQuery(self, text):
        text = [nlp.filterText(text)]
        pprint(text)
        self.tokenizer.fit_on_texts(text)
        text = self.tokenizer.texts_to_sequences(text)
        text = pad_sequences(text, padding='post', maxlen=self.maxLen)
        return text

    def getPredictedTopics(self, text):
        # Compress strings to numbers
        X_test = self.instantiateQuery(text)
        Y_predictions = self.model.predict(X_test)
        pprint(Y_predictions)
        pprint(self.reverseTopicMap)
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
            predictedTopics.append(self.reverseTopicMap[i])

        return predictedTopics
