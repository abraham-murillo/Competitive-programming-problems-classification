from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from api import getAll
from api import nlp
# import pandas as pd
# import numpy as np
from numpy import asarray
# from numpy import zeros
from pprint import pprint

# import re
# import ntk
# from nltk.corpus import stopwords

from numpy import array
from keras_preprocessing.sequence import pad_sequences
from tensorflow.keras import Sequential
from keras.layers.core import Activation, Dropout, Dense
from keras.layers import Flatten, Conv1D, LSTM, GlobalMaxPooling1D
from tensorflow.keras.layers import Embedding

import matplotlib.pyplot as plt


def train():
    allProblems = getAll()[:10]
    X = []

    for problemData in allProblems:
        description = problemData["history"]
        description = nlp.filterText(description)
        X.append(description)

    Y = []
    id = {}

    for problemData in allProblems:
        target = problemData["topics"][0]["id"]

        if target not in id:
            id[target] = len(id)

        Y.append(id[target])

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)

    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(X_train)
    X_train = tokenizer.texts_to_sequences(X_train)
    X_test = tokenizer.texts_to_sequences(X_test)

    maxLen = 100

    X_train = pad_sequences(X_train, padding='post', maxlen=maxLen)
    X_test = pad_sequences(X_test, padding='post', maxlen=maxLen)

    # # TODO: Find a place to store Word2Vect and use it here
    embeddings = dict()
    embeddingsFile = open("/home/uriel/CUCEI/Word2VecEnglish.txt", "r")

    for line in embeddingsFile:
        features = line.split()
        word = features[0]
        vector = asarray(features[1:], dtype='float32')
        embeddings[word] = vector

    embeddingsFile.close()
    vocabSize = len(tokenizer.word_index) + 1
    embeddingMatrix = zeros((vocabSize, 300))

    for word, index in tokenizer.word_index.items():
        embeddingVector = embeddings.get(word)

        if embeddingVector is not None:
            embeddingMatrix[index] = embeddingVector

    model = Sequential()
    embeddingLayer = Embedding(vocabSize, 300, weights=[
                               embeddingMatrix], input_length=maxLen, trainable=False)
    model.add(embeddingLayer)
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam',
                  loss='binary_crossentropy', metrics=['acc'])

    history = model.fit(X_train, np.array(Y_train), batch_size=128,
                        epochs=10, verbose=1, validation_split=0.2)
    score = model.evaluate(X_test, np.array(Y_test), verbose=1)
    print("Test Loss:", score[0])
    print("Test Accuracy:", score[1])


train()
