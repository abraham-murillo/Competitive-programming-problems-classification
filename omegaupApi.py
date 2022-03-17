import urllib.request

from pylatexenc.latex2text import LatexNodes2Text
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

from pprint import pprint
import json


def getFrom(url):
    url = url.replace(' ', '%20')
    driver = webdriver.Chrome()
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    if url.startswith("https://omegaup.com/arena/problem/"):
        # Extract omegaup problem data from html
        problem = {}

        allText = ""
        for html in soup.findAll('div', attrs={'class': 'mt-4 markdown'}):
            allText += html.text
        allText += "Fin\n"
        allText = allText.split('\n')

        problemSections = {
            'Descripción': 'history',
            'Entrada': 'input',
            'Salida': 'output',
            'Ejemplo': '?',
            'Notas': 'note',
            'Fin': '?',
        }

        section = ""
        doing = "?"
        for text in allText:
            text = text.strip()
            text = LatexNodes2Text().latex_to_text(text)
            print(text)
            if text in problemSections:
                if doing != '?':
                    problem[doing] = section
                doing = problemSections[text]
                section = ""
            else:
                section += text

        problem['url'] = url

        return problem
    elif url.startswith("https://omegaup.com/problem/list"):
        # Extract all problemset
        problems = soup.find('script', attrs={'id': 'payload'})
        problems = json.loads(problems.contents[0])['problems']

        tagPrefixes = ['problemTag', 'problemTopic']

        def destroyCamelCase(text):
            for prefix in tagPrefixes:
                if text.startswith(prefix):
                    text = text[len(prefix):]

            answer = ""
            for ch in text:
                if ch.isupper() and len(answer):
                    answer += ' '
                answer += ch.lower()

            return answer.lower()

        return [{
            'url': problem['alias'],
            'name': problem['title'],
            'id': problem['problem_id'],
            'site': 'omegaup',
            'tags': [destroyCamelCase(tag['name'])
                     for tag in problem['tags']
                     if any(tag['name'].startswith(prefix) for prefix in tagPrefixes)],
        } for problem in problems]


def getAllTags():
    # omegaupTags.txt was extracted by hand :'(
    tags = dict()
    count = dict()
    with open("omegaupTags.txt") as input:
        level = 0
        for line in input.readlines():
            line = line.strip()
            if line.isdigit():
                level = int(line)
            elif len(line) > 0:
                if line not in tags:
                    tags[line] = level
                    count[line] = 1
                else:
                    tags[line] += level
                    count[line] += 1

    # Aproximate to codeforces rating
    # Sort tags by average rating (in theory those are easier)
    tags = [(tag.lower(), rating * 900 / count[tag])
            for tag, rating in tags.items()]
    return sorted(tags, key=lambda x: x[1])


def getProblem(problem):
    url = f"https://omegaup.com/arena/problem/{problem['url']}"
    problem.update(getFrom(url))
    return problem


def getProblemset(tagsRating, maxNumOfProblems=-1):
    """
    Returns the omegaup problemset
        - All problems should have at least 1 of the tags
        - Rating of the problem (if any) should be smaller than maxRating
        - limit of problems is maxNumOfProblems
    """

    tagsSet = set()
    for tag, rating in tagsRating:
        tagsSet.add(tag)

    # Filter the problemset, if problem[tag] isn't in tags ignore the problem
    filteredProblems = dict()

    def enoughProblems():
        return maxNumOfProblems != -1 and len(filteredProblems) >= maxNumOfProblems

    def getProblems(tag, page):
        tag = "".join(word.title() for word in tag.split())
        url = f"https://omegaup.com/problem/list/?page={page}&tag[]=problemTag{tag}"
        return getFrom(url)

    for tag, rating in tagsRating:
        for page in range(0, 1000):
            problemsWithATag = getProblems(tag, page)
            # print(len(problemsWithATag))

            for problem in problemsWithATag:
                filteredProblems[problem['id']] = problem

                if enoughProblems():
                    break

            if enoughProblems():
                break

            # Apparently if it has less than 100 problems per page it's the last pagination index
            if len(problemsWithATag) < 100:
                break

        if enoughProblems():
            break

    # pprint.pprint(filteredProblems)
    return filteredProblems


# List obtained with getAllTags()
tagsRating = [('formatted input and output', 900.0),
              ('brute force', 900.0),
              ('functions', 900.0),
              ('analytic geometry', 900.0),
              ('loops', 1800.0),
              ('arithmetic', 1800.0),
              ('conditionals', 1800.0),
              ('input and output', 1800.0),
              ('matrices', 1800.0),
              ('omi', 1800.0),
              ('stacks', 1800.0),
              ('queues', 1800.0),
              ('disjoint sets', 1800.0),
              ('binary search tree', 1800.0),
              ('tree traversal', 1800.0),
              ('divide and conquer', 1800.0),
              ('memorization', 1800.0),
              ('recursion', 1800.0),
              ('backtracking', 1800.0),
              ('greedy algorithms', 1800.0),
              ('modular arithmetic', 1800.0),
              ('sliding window', 1800.0),
              ('analysis of recurrences', 1800.0),
              ('number theory', 1800.0),
              ('common multiples and divisors', 1800.0),
              ('primality test', 1800.0),
              ('prime generation', 1800.0),
              ('counting problems', 1800.0),
              ('big numbers', 1800.0),
              ('chars and strings', 1950.0),
              ('arrays', 1980.0),
              ('sorting', 1980.0),
              ('implementation', 2025.0),
              ('binary search', 2025.0),
              ('dynamic programming', 2250.0),
              ('breadth-first search', 2250.0),
              ('depth-first search', 2250.0),
              ('graph representation', 2250.0),
              ('hashing', 2250.0),
              ('bit manipulation', 2250.0),
              ('segment trees', 2700.0),
              ('fenwick trees', 2700.0),
              ('big data', 2700.0),
              ('unformatted input and output', 2700.0),
              #   ('file seeking', 2700.0),
              ('data compression', 2700.0),
              ('lexing and parsing', 2700.0),
              ('heuristics', 2700.0)]
