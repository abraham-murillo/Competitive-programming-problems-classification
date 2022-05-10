import codeforcesApi
import omegaupApi
import json
from pprint import pprint

punctuation = "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"


def fixData(problem):
    # Add spaces before new sentences
    def addSpaces(text):
        newText = ""
        last = ''
        for ch in text:
            if last in punctuation:
                newText += " "
            newText += ch
            last = ch

        return text

    for field in ['history', 'input', 'output', 'note']:
        if field in problem:
            problem[field] = addSpaces(problem[field])

    return problem


def getCodeforcesProblems(numOfProblems):
    # 5 easy tags
    easyTags = codeforcesApi.tagsRating[0:5]
    problems = codeforcesApi.getProblemset(easyTags, numOfProblems)

    for id, data in problems.items():
        data = codeforcesApi.getProblem(data)
        jsonData = json.dumps(fixData(data), indent=4)
        # pprint(data)

        with open(f"problems/{id}.json", "w") as outfile:
            outfile.write(jsonData)


def getOmegaupProblems(numOfProblems):
    # 5 easy tags
    easyTags = omegaupApi.tagsRating[0:5]
    problems = omegaupApi.getProblemset(easyTags, numOfProblems)

    for id, data in problems.items():
        data = omegaupApi.getProblem(data)
        jsonData = json.dumps(fixData(data), indent=4)
        # pprint(data)

        with open(f"problems/{id}.json", "w") as outfile:
            outfile.write(jsonData)


getCodeforcesProblems(10)
getOmegaupProblems(10)
