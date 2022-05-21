import spacy
from pprint import pprint
import json


class SmartNLP():
    # TODO: Enable both english and spanish nlp
    english = spacy.load("en_core_web_sm")
    spanish = spacy.load("es_core_news_sm")

    def detectLanguage(self, text):
        # Returns nlp based on the language
        return self.english


smart = SmartNLP()


def tokenize(text):
    nlp = smart.detectLanguage(text)
    text = nlp(text)

    tokens = dict()
    for word in text:
        tokens[word.lemma_] = {
            "text": word.text,
            "pos": word.pos_,
            "lemma": word.lemma_,
            "tag": word.tag_,
            "dep": word.dep_,
            "stop": word.is_stop
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


def filterText(text):
    lemmatizedText = lemmatize(text)
    return lemmatizedText


# text = "I am the green child. Behold! a green child is here! Denounce the all-mighty taurus and begone my young ones!"
# texts = {"Text1": "Hello, how are you?",
#          "Text2": "I'm fine, and you",
#          "Text3": "Fine as well, thank you!"}
# pprint(featureMatrix(texts))
