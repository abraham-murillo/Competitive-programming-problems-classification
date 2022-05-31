import spacy
from pprint import pprint
from langdetect import detect
import re

import unicodedata
from pylatexenc.latex2text import LatexNodes2Text

import pandas
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


class SmartNLP():
    english = spacy.load("en_core_web_sm")
    spanish = spacy.load("es_core_news_sm")

    def detectLanguage(self, text):
        # Returns nlp based on the language
        # return self.english if detect(text) == "en" else self.spanish
        return self.english


smart = SmartNLP()


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
    text = unicodedata.normalize('NFKD', text)
    text = lemmatize(text)
    # Remove multiple spaces
    text = re.sub(' +', ' ', text)
    # Remove newlines
    text = text.replace("\n", "")
    # Remove stopwords in spanish
    spanishStopWords = ['a', 'acá', 'ahí', 'al', 'algo', 'algún', 'alguna', 'alguno', 'algunas', 'algunos', 'allá', 'allí', 'ambos', 'ante',
                        'antes', 'aquel', 'aquella', 'aquello', 'aquellas', 'aquellos', 'aquí', 'arriba', 'así', 'atrás', 'aun', 'aunque',
                        'bien', 'cada', 'casi', 'como', 'con', 'cual', 'cuales', 'cualquier', 'cualquiera', 'cuan', 'cuando', 'cuanto', 'cuanta',
                        'cuantos', 'cuantas', 'de', 'del', 'demás', 'desde', 'donde', 'dos', 'el', 'él', 'ella', 'ello', 'ellas', 'ellos', 'en',
                        'eres', 'esa', 'ese', 'eso', 'esas', 'esos', 'esta', 'esto', 'estas', 'estos', 'este', 'etc', 'ha', 'hasta', 'la', 'lo', 'las',
                        'los', 'me', 'mi', 'mis', 'mía', 'mías', 'mío', 'míos', 'mientras', 'muy', 'ni', 'nosotras', 'nosotros', 'nuestra',
                        'nuestro', 'nuestras', 'nuestros', 'os', 'otra', 'otro', 'otras', 'otros', 'para', 'pero', 'pues', 'que', 'qué', 'si', 'sí',
                        'siempre', 'siendo', 'sin', 'sino', 'so', 'sobre', 'sr', 'sra', 'sres', 'sta', 'su', 'sus', 'te', 'tu', 'tus', 'un', 'una',
                        'uno', 'unas', 'unos', 'usted', 'ustedes', 'vosotras', 'vosotros', 'vuestra', 'vuestro', 'vuestras', 'vuestros', 'y', 'ya',
                        'yo']

    for stopWord in spanishStopWords:
        text = text.replace(" " + str(stopWord) + " ", " ")

    return text


def featureMatrix(texts):
    nlpTexts = {}

    # Convert each text to nlp form
    for label in texts.keys():
        nlp = smart.detectLanguage(texts[label])
        nlpTexts[label] = nlp(texts[label])

    vocabulary = {}

    # Exatract vocabulary
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
# tfIdfImportant(texts)
