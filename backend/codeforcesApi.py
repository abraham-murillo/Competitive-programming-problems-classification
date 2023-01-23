import urllib.request

from bs4 import BeautifulSoup
import SmartRequests

from pprint import pprint
import json


def getFrom(url):
    url = url.replace(" ", "%20")

    if url.startswith("https://codeforces.com/api/"):
        # https://codeforces.com/apiHelp/
        # Easy request using codeforces api
        page = urllib.request.urlopen(url)
        return json.loads(str(BeautifulSoup(page, "html.parser")))
    elif url.startswith("https://codeforces.com/problemset/problem/"):
        # Extract codeforces problem data from html
        request = SmartRequests.get(url)
        if request is None:
            return {}

        content = request.content
        soup = BeautifulSoup(content, "html.parser")

        problem = {}
        problem["url"] = url

        def decomposeIfFound(html):
            if html:
                html.decompose()

        try:
            for html in soup.findAll("div", attrs={"class": "problem-statement"}):
                decomposeIfFound(html.find("div", attrs={"class": "header"}))
                decomposeIfFound(html.find("div", attrs={"class": "sample-tests"}))

                input = html.find("div", attrs={"class": "input-specification"})
                if input:
                    decomposeIfFound(
                        input.find("div", attrs={"class": "section-title"})
                    )
                    problem["input"] = input.text

                output = html.find("div", attrs={"class": "output-specification"})
                if output:
                    decomposeIfFound(
                        output.find("div", attrs={"class": "section-title"})
                    )
                    problem["output"] = output.text
                note = html.find("div", attrs={"class": "note"})
                if note:
                    decomposeIfFound(note.find("div", attrs={"class": "section-title"}))
                    problem["note"] = note.text
                decomposeIfFound(
                    html.find("div", attrs={"class": "input-specification"})
                )
                decomposeIfFound(
                    html.find("div", attrs={"class": "output-specification"})
                )
                decomposeIfFound(html.find("div", attrs={"class": "note"}))

            problem["history"] = html.text
        except:
            print(f"Problem {url} failed to load")

        return problem


def getAllTopics():
    """
    Returns topics sorted by average rating
    """
    url = "https://codeforces.com/api/problemset.problems"
    problems = getFrom(url)["result"]["problems"]

    tags = dict()
    for problem in problems:
        for tag in problem["tags"]:
            rating = tags.get(tag, {"count": 0, "sum": 0})
            if "rating" in problem:
                rating["count"] += 1
                rating["sum"] += problem["rating"]
            tags[tag] = rating

    # Sort tags by average rating (in theory those are easier)
    tags = [(tag, rating["sum"] / rating["count"]) for tag, rating in tags.items()]
    return sorted(tags, key=lambda x: x[1])


def getProblem(problem):
    """
    Default problem definition:
        {'contestId': 1000,
        'index': 'A',
        'name': 'Codehorses T-shirts',
        'rating': 1200,
        'tags': ['greedy', 'implementation'],
        'type': 'PROGRAMMING'},
    """

    url = f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']}"
    data = getFrom(url)
    problem.update(data)
    return problem


def getProblemset(topics, maxNumOfProblems=-1):
    """
    Returns the codeforces problemset
        - All problems should have at least 1 of the tags
        - limit of problems is maxNumOfProblems
    """

    def getProblems(tag):
        url = f"https://codeforces.com/api/problemset.problems?tags={tag}"
        return getFrom(url)["result"]["problems"]

    problems = dict()

    def enoughProblems():
        return maxNumOfProblems != -1 and len(problems) >= maxNumOfProblems

    for topic in topics:
        problemsWithTopic = getProblems(topic)
        # print(len(problemsWithTopic))

        for problem in problemsWithTopic:
            problemId = str(problem["contestId"]) + problem["index"]
            problem["id"] = problemId
            problem["site"] = "codeforces"
            problems[problemId] = problem

            if enoughProblems():
                break

        # print(len(problems))
        if enoughProblems():
            break

    # pprint(problems)
    return problems


# List obtained with getAllTopics()
topicsRating = [
    ("implementation", 1480.7348092322186),
    ("sortings", 1734.078947368421),
    ("strings", 1734.0740740740741),
    ("greedy", 1721.7074440395627),
    ("number theory", 1917.490494296578),
    ("brute force", 1730.524505588994),
    ("math", 1769.0954773869346),
    ("expression parsing", 1862.5),
    ("constructive algorithms", 1865.944540727903),
    ("schedules", 1883.3333333333333),
    ("two pointers", 1964.207650273224),
    ("ternary search", 2020.4545454545455),
    ("binary search", 2045.6258411843876),
    ("games", 2072.972972972973),
    ("dfs and similar", 2144.7214076246332),
    ("dsu", 2160.8695652173915),
    ("bitmasks", 2176.2162162162163),
    ("dp", 2191.527599486521),
    ("combinatorics", 2213.3037694013306),
    ("geometry", 2222.257053291536),
    ("shortest paths", 2225.0),
    ("graphs", 2253.4969325153374),
    ("hashing", 2275.641025641026),
    ("data structures", 2295.8870967741937),
    ("meet-in-the-middle", 2357.8947368421054),
    ("trees", 2383.505154639175),
    ("chinese remainder theorem", 2384.6153846153848),
    ("2-sat", 2400.0),
    ("probabilities", 2400.5555555555557),
    ("interactive", 2420.0),
    ("graph matchings", 2440.909090909091),
    ("matrices", 2495.8333333333335),
    ("divide and conquer", 2536.3636363636365),
    ("flows", 2543.362831858407),
    ("string suffix structures", 2612.987012987013),
    ("fft", 2865.217391304348),
]
