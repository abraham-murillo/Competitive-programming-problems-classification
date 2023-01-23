import CodeforcesApi
import OmegaupApi
import json
from pprint import pprint
from string import punctuation
import unicodedata
from pylatexenc.latex2text import LatexNodes2Text
from topicsStandardization import getOmegaupTopics, getCodeforcesTopics

from random import random
from time import sleep
from multiprocessing import Pool
import itertools

import SmartRequests
from datetime import datetime
import os

PROCESSES = 30
BUCKET_SIZE = 100


def flatten(t):
    return [item for sublist in t for item in sublist]


def addSpaces(text):
    newText = ""
    last = ""
    for ch in text:
        if last in punctuation:
            newText += " "
        newText += ch
        last = ch
    return newText


def pretty(text):
    text = LatexNodes2Text().latex_to_text(text)
    text = unicodedata.normalize("NFKD", text)
    text = addSpaces(text)
    return " ".join(text.split())


def fixData(problem):
    for field in ["history", "input", "output", "note"]:
        if field in problem:
            problem[field] = pretty(problem[field])
        else:
            problem[field] = ""
    # pprint(problem)

    # Extract only important problem data
    return {
        "title": problem["name"],
        "url": problem["url"],
        "history": problem["history"],
        "input": problem["input"],
        "output": problem["output"],
        "note": problem["note"],
        "topics": problem["tags"],
        "id": problem["id"] if "id" in problem else "?",
    }


def saveProblems(fileName, problems):
    file = open(f"{fileName}", "w")
    json.dump(problems, file, indent=2)
    file.close()
    print(f"File {fileName} is ready with {len(problems)} problems\n")


def getCodeforcesProblem(data):
    return fixData(CodeforcesApi.getProblem(data))


def getCodeforcesProblems(topic, numOfProblems):
    dataSetName = f"data/codeforces-{topic}.json"

    problemset = CodeforcesApi.getProblemset([topic], numOfProblems)
    allProblems = []

    print(f"The problemset of {topic} consists of {len(problemset)} problems")

    if os.path.isfile(dataSetName):
        # As the file already exists, try to collect only the problems that are missing of a history
        print(f"File {dataSetName} exists, loading stored data...")
        allProblems = json.load(open(dataSetName))

        # In case some problems where stored empty, fill them
        allProblemsCopy = []
        for index, problem in enumerate(allProblems):
            history = problem["history"]
            if (
                len(problem["history"]) + len(problem["input"]) + len(problem["output"])
                > 0
            ):
                # As the problem has data, remove it from the problemset
                url = problem["url"].split("/")
                id = url[-2] + url[-1]
                problemset.pop(id, "?")
                allProblemsCopy.append(problem)

        allProblems = allProblemsCopy

    problemsetValues = list(problemset.values())
    problemsetValues = problemsetValues[0:500]

    print(f"Doing data scraping of {len(problemsetValues)} problems")
    batches = [
        problemsetValues[i : i + BUCKET_SIZE]
        for i in range(0, len(problemsetValues), BUCKET_SIZE)
    ]

    # Run in parallel the data-scraping
    for index, batch in enumerate(batches):
        print(
            f"Doing batch {index+1}/{len(batches)}..., total problems collected so far is {len(allProblems)}, aiming to collect {len(batch)} new problems"
        )
        with Pool(processes=PROCESSES) as pool:
            problems = pool.map(getCodeforcesProblem, batch)
        allProblems.extend(problems)

    saveProblems(dataSetName, allProblems)


def getOmegaupProblem(data):
    data = fixData(OmegaupApi.getProblem(data))
    codeforcesTopics = set(flatten([getCodeforcesTopics(x) for x in data["topics"]]))
    data["topics"] = list(codeforcesTopics)
    return data


def getOmegaupProblems(topic, numOfProblems):
    dataSetName = f"data/omegaup-{topic}.json"

    omegaupTopics = getOmegaupTopics(topic)
    problemset = OmegaupApi.getProblemset(omegaupTopics, numOfProblems)
    allProblems = []

    print(f"The problemset of {topic} consists of {len(problemset)} problems")

    if os.path.isfile(dataSetName):
        # As the file already exists, try to collect only the problems that are missing of a history
        print(f"File {dataSetName} exists, loading stored data...")
        allProblems = json.load(open(dataSetName))

        allProblemsCopy = []
        # In case some problems where stored empty, fill them
        for index, problem in enumerate(allProblems):
            if (
                len(problem["history"]) + len(problem["input"]) + len(problem["output"])
                > 0
            ):
                # As the problem has data, remove it from the problemset
                id = problem["id"]
                problemset.pop(id, "?")
                allProblemsCopy.append(problem)

        allProblems = allProblemsCopy

    problemsetValues = list(problemset.values())

    print(f"Doing data scraping of {len(problemsetValues)} problems")

    batches = [
        problemsetValues[i : i + BUCKET_SIZE]
        for i in range(0, len(problemsetValues), BUCKET_SIZE)
    ]

    # Run in parallel the data-scraping
    for index, batch in enumerate(batches):
        print(
            f"Doing batch {index+1}/{len(batches)}..., total problems collected so far is {len(allProblems)}, aiming to collect {len(batch)} new problems"
        )
        with Pool(processes=PROCESSES) as pool:
            problems = pool.map(getOmegaupProblem, batch)
        allProblems.extend(problems)

    saveProblems(dataSetName, allProblems)


# This are the topics to start training
startingTopics = [
    "sortings",
    "strings",
    "greedy",
    "number theory",
    "math",
    "graphs",
    "geometry",
    "data structures",
]

if __name__ == "__main__":
    numOfProblems = 1500
    topics = startingTopics

    for topic in topics:
        start = datetime.now()
        print(topic)
        # getCodeforcesProblems(topic, numOfProblems)
        getOmegaupProblems(topic, numOfProblems)
        end = datetime.now() - start
        print(f"It took {end} to collect {topic}'s problems\n")
