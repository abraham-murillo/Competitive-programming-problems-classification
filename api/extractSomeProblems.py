import codeforcesApi
import omegaupApi
from api import addProblem
import json
from pprint import pprint

from string import punctuation

import unicodedata
from pylatexenc.latex2text import LatexNodes2Text
from topicsStandardization import getOmegaupTopics, getCodeforcesTopics


def flatten(t):
    return [item for sublist in t for item in sublist]

def fixData(problem):
    def addSpaces(text):
        newText = ""
        last = ''
        for ch in text:
            if last in punctuation:
                newText += " "
            newText += ch
            last = ch
        return newText

    def pretty(text):
        text = LatexNodes2Text().latex_to_text(text)
        text = unicodedata.normalize('NFKD', text)
        text = addSpaces(text)
        return " ".join(text.split())

    for field in ['history', 'input', 'output', 'note']:
        if field in problem:
            problem[field] = pretty(problem[field])
        else:
            problem[field] = " "

    # Extract only important problem data
    return {
        "title": problem["name"],
        "url": problem["url"],
        "history": problem["history"],
        "input": problem["input"],
        "output": problem["output"],
        "note": problem["note"],
        "topics": problem["tags"],
    }


def getCodeforcesProblems(topic, numOfProblems):
    problemset = codeforcesApi.getProblemset([topic], numOfProblems)
    for id, data in problemset.items():
        data = fixData(codeforcesApi.getProblem(data))
        addProblem(data)

def getOmegaupProblems(topic, numOfProblems):
    topic = topic[0]
    omegaupTopics = getOmegaupTopics(topic)

    problemset = omegaupApi.getProblemset(omegaupTopics, numOfProblems)
    for id, data in problemset.items():
        data = fixData(omegaupApi.getProblem(data))
        codeforcesTopics = set(flatten([getCodeforcesTopics(x) for x in data['topics']]))
        data['topics'] = list(codeforcesTopics)  
        addProblem(data) 

last = 0

numOfProblems = 1
topics = codeforcesApi.topicsRating[last : last + 3]

for topic in topics:
    print(topic)
    getCodeforcesProblems(topic, numOfProblems)
    getOmegaupProblems(topic, numOfProblems)

print("Done")

codeforcesApi.driver.close()
omegaupApi.driver.close()