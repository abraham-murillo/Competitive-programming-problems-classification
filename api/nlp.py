import spacy
from pprint import pprint
from langdetect import detect
import re

import unicodedata
from pylatexenc.latex2text import LatexNodes2Text

import pandas
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


class SmartNLP:
    english = spacy.load("en_core_web_sm")
    spanish = spacy.load("es_core_news_sm")

    def detectLanguage(self, text):
        # Returns nlp based on the language
        # return self.english if detect(text) == "en" else self.spanish
        return self.english


smart = SmartNLP()


def textSet(text):
    text = filterText(text)
    words = set(text.split())
    return words


def sentences(text):
    nlp = smart.detectLanguage(text)
    text = nlp(text)
    return [i.text.strip() for i in text.sents]


# text = "In the popular spreadsheets systems (for example, in Excel) the following numeration of columns is used. The first column has number A, the second — number B, etc. till column 26 that is marked by Z. Then there are two-letter numbers: column 27 has number AA, 28 — AB, column 52 is marked by AZ. After ZZ there follow three-letter numbers, etc.The rows are marked by integer numbers starting with 1. The cell name is the concatenation of the column and the row numbers. For example, BC23 is the name for the cell that is in column 55, row 23. Sometimes another numeration system is used: RXCY, where X and Y are integer numbers, showing the column and the row numbers respectfully. For instance, R23C55 is the cell from the previous example."
# pprint(sentences(text))


def tokenize(text):
    nlp = smart.detectLanguage(text)
    text = nlp(text)

    tokens = dict()
    for word in text:
        tokens = {
            "text": word.text,
            "pos": word.pos_,
            "lemma": word.lemma_,
            "tag": word.tag_,
            "dep": word.dep_,
            "stop": word.is_stop,
        }

    return list(tokens.values())


# text = "hello, how are you?"
# pprint(tokenize(text))


def lemmatize(text):
    nlp = smart.detectLanguage(text)
    text = nlp(text)
    lemmatizedText = str()

    for word in text:
        if not word.is_punct and not word.is_stop:
            lemmatizedText += word.lemma_.lower() + " "

    return lemmatizedText[:-1]


def filterText(text):
    text = LatexNodes2Text().latex_to_text(text)
    text = unicodedata.normalize("NFKD", text)
    text = lemmatize(text)
    # Remove multiple spaces
    text = re.sub(" +", " ", text)
    # Remove newlines
    text = text.replace("\n", "")
    return text


def featureMatrix(texts):
    nlpTexts = {}

    # Convert each text to nlp form
    for label in texts.keys():
        nlp = smart.detectLanguage(texts[label])
        nlpTexts[label] = nlp(texts[label])

    vocabulary = {}

    # Extract vocabulary
    for text in nlpTexts.values():
        for token in text:
            if token.text.lower() not in vocabulary:
                vocabulary[token.text.lower()] = len(vocabulary)

    features = []

    # Add labels
    for label in nlpTexts.keys():
        features.append([label] + [0] * len(vocabulary))

    i = 0

    # Count token frequencies
    for text in nlpTexts.values():
        for token in text:
            features[i][vocabulary[token.text.lower()] + 1] += 1

        i += 1

    return features


# text = "I am the green child. Behold! a green child is here! Denounce the all-mighty taurus and begone my young ones!"
# texts = {"Text1": "Hello, how are you?",
#          "Text2": "I'm fine, and you",
#          "Text3": "Fine as well, thank you!"}
# pprint(featureMatrix(texts))


def tfIdfMatrix(texts):
    """
    TF-IDF is a scoring measure widely used in information retrieval (IR) or summarization. TF-IDF is intended to reflect how relevant a term is in a given document.
        - A data cleansing technique should be applied to the texts in advance.
    """
    cv = CountVectorizer()
    wordsCount = cv.fit_transform(texts)

    data = TfidfVectorizer().fit_transform(texts)
    data = pandas.DataFrame(
        data.todense(),
        index=[i for i in range(0, len(texts))],
        columns=cv.get_feature_names_out(),
    )

    return data


# Example extracted from https://medium.datadriveninvestor.com/tf-idf-in-natural-language-processing-8db8ef4a7736
# texts = ["eat veg", "eat nonveg", "eat food"]
# pprint(tfIdf(texts))


def moreImportant(texts, keepQuantileAbove=0.3):
    """
    Returns the texts after filtering NON important words
    - Extracts tdIdf matrix, if the tdIdfValue[word] is part of the top quantile that makes the word been considered as important
    - keepQuantileAbove is a percentage in [0, 1] that indicates the percentage of the values of the quantile that we want to keep
    """
    # https://programminghistorian.org/en/lessons/analyzing-documents-with-tfidf

    # Filter stopwords and lemmatize
    texts = [filterText(text) for text in texts]

    # Generate tf-idf matrix
    tfIdf = tfIdfMatrix(texts)

    quantile = tfIdf.quantile(keepQuantileAbove)
    # Which words I'm using
    wordsSet = set()
    for word in tfIdf:
        # print(word, quantile[word]) # quantile value for each word
        wordsSet.add(word)

    n, m = tfIdf.shape
    important = []
    for i in range(0, n):
        tfIdfValue = tfIdf.iloc[i]

        words = texts[i].split()
        # For all words of text[i] keep them only if they are important
        words = [
            word
            for word in words
            if word in wordsSet and tfIdfValue[word] > quantile[word]
        ]
        important.append(" ".join(words))

    return important


def lessImportantWords(texts, keepQuantileBelow=0.3):
    """
    Returns less important words for each text
    - keepQuantileBelow is a percentage in [0, 1] that indicates the percentage of the values of the quantile that we DON'T want to keep
    """
    important = moreImportant(texts, keepQuantileBelow + 0.001)

    trash = []
    for i, text in enumerate(texts):
        before = textSet(text)
        after = textSet(important[i])
        trash.append(before.difference(after))

    return trash


# texts = [
#     "Theatre Square in the capital city of Berland has a rectangular shape with the size nxm meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size axa.What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.",
#     "In the popular spreadsheets systems (for example, in Excel) the following numeration of columns is used. The first column has number A, the second — number B, etc. till column 26 that is marked by Z . Then there are two-letter numbers: column 27 has number AA, 28 — AB, column 52 is marked by AZ. After ZZ there follow three-letter numbers, etc.The rows are marked by integer numbers starting with 1. The cell name is the concatenation of the column and the row numbers. For example, BC23 is the name for the cell that is in column 55, row 23. Sometimes another numeration system is used: RXCY, where X and Y are integer numbers, showing the column and the row numbers respectfully. For instance, R23C55 is the cell from the previous example. Your task is to write a program that reads the given sequence of cell coordinates and produce each item written according to the rules of another numeration system.",
#     "Nowadays all circuses in Berland have a round arena with diameter 13 meters, but in the past things were different. In Ancient Berland arenas in circuses were shaped as a regular (equiangular) polygon, the size and the number of angles could vary from one circus to another. In each corner of the arena there was a special pillar, and the rope strung between the pillars marked the arena edges. Recently the scientists from Berland have discovered the remains of the ancient circus arena. They found only three pillars, the others were destroyed by the time. You are given the coordinates of these three pillars. Find out what is the smallest area that the arena could have.",
# ]

# pprint(moreImportant(texts, 0.3))
# pprint(lessImportantWords(texts, 0.3))
