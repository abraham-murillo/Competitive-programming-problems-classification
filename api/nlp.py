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
