import urllib.request

from webdriver_manager.chrome import ChromeDriverManager
from pylatexenc.latex2text import LatexNodes2Text
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# import trashTags
from pprint import pprint
import json

driver = webdriver.Chrome(ChromeDriverManager().install())
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


def getFrom(url):
    url = url.replace(' ', '%20')
    
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

        return [{
            'url': problem['alias'],
            'name': problem['title'],
            'id': problem['problem_id'],
            'site': 'omegaup',
            'tags': [destroyCamelCase(tag['name'])
                     for tag in problem['tags']
                     if any(tag['name'].startswith(prefix) for prefix in tagPrefixes)],
        } for problem in problems]


# def getAllTags():
#     # omegaupTags.txt was extracted by hand :'(
#     tags = dict()
#     count = dict()
#     with open("omegaupTags.txt") as input:
#         level = 0
#         for line in input.readlines():
#             line = line.strip()
#             if line.isdigit():
#                 level = int(line)
#             elif len(line) > 0:
#                 line = line.lower()
#                 if line not in tags:
#                     tags[line] = level
#                     count[line] = 1
#                 else:
#                     tags[line] += level
#                     count[line] += 1

#     for tag, level in trashTags.tags:
#         tag = destroyCamelCase(tag).lower()
#         if tag not in tags:
#             tags[tag] = level
#             count[tag] = 1

#     # Aproximate to codeforces rating
#     # Sort tags by average rating (in theory those are easier)
#     tags = [(tag.lower(), round(rating * 900 / count[tag], 2))
#             for tag, rating in tags.items()]
#     return sorted(tags, key=lambda x: x[1])


def getProblem(problem):
    url = f"https://omegaup.com/arena/problem/{problem['url']}"
    problem.update(getFrom(url))
    return problem


def getProblemset(topics, maxNumOfProblems=-1):
    """
    Returns the omegaup problemset
        - All problems should have at least 1 of the topics
        - limit of problems is maxNumOfProblems
    """

    filteredProblems = dict()

    def enoughProblems():
        return maxNumOfProblems != -1 and len(filteredProblems) >= maxNumOfProblems

    def getProblems(tag, page):
        tag = "".join(word.title() for word in tag.split())
        url = f"https://omegaup.com/problem/list/?page={page}&tag[]=problemTag{tag}"
        return getFrom(url)

    for topic in topics:
        for page in range(0, 1000):
            problemsWithTopic = getProblems(topic, page)
        
            for problem in problemsWithTopic:
                filteredProblems[problem['id']] = problem

                if enoughProblems():
                    break

            if enoughProblems():
                break

            # Apparently if it has less than 100 problems per page it's the last pagination index
            if len(problemsWithTopic) < 100:
                break

        if enoughProblems():
            break

    # pprint.pprint(filteredProblems)
    return filteredProblems


# List obtained with getAllTags()
topicsRating = [('formatted input and output', 900.0),
              ('brute force', 900.0),
              ('functions', 900.0),
              ('analytic geometry', 900.0),
              ('simulation', 900.0),
              ('gcd and lcm', 900.0),
              ('partial sums', 900.0),
              ('prime factorization', 900.0),
              ('exponential search', 900.0),
              ('tree tranversal', 900.0),
              ('breadth first search', 900.0),
              ('depth first search', 900.0),
              ('disjoint sets', 900.0),
              ('inverted indices', 900.0),
              ('incremental search', 900.0),
              ('local search', 900.0),
              ('meet in the middle', 900.0),
              ('bipartite matching', 900.0),
              ('divisibility rules', 1170.0),
              ('combinatorial designs', 1440.0),
              ('numerical series', 1440.0),
              ('exponentiation by squaring', 1440.0),
              ('shortest paths', 1440.0),
              ('minimum spanning trees', 1440.0),
              ('sub array search', 1440.0),
              ('subsequence search', 1440.0),
              ('monotone stack', 1440.0),
              ('two pointers technique', 1440.0),
              ('combinations', 1530.0),
              ('heaps', 1530.0),
              ('graph connectivity', 1530.0),
              ('trees', 1530.0),
              ('topological sorting', 1530.0),
              ('wavelet trees', 1530.0),
              ('loops', 1800.0),
              ('arithmetic', 1800.0),
              ('conditionals', 1800.0),
              ('input and output', 1800.0),
              ('matrices', 1800.0),
              ('stacks', 1800.0),
              ('queues', 1800.0),
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
              ('systems of equations', 1800.0),
              ('diophantine equations', 1800.0),
              ('modular multiplicative inverse', 1800.0),
              ('chinese remainder theorem', 1800.0),
              ('permutations', 1800.0),
              ('game theory', 1800.0),
              ('probability and statistics', 1800.0),
              ('string matching', 1800.0),
              ('linked lists', 1800.0),
              ('directed graphs', 1800.0),
              ('graphs with negative weights', 1800.0),
              ('tries', 1800.0),
              ('least common ancestor', 1800.0),
              ('offline queries', 1800.0),
              ('sqrt decomposition', 1800.0),
              ('nearest neighbors', 1800.0),
              ('chars and strings', 1950.0),
              ('arrays', 1980.0),
              ('sorting', 1980.0),
              ('fourier transformation', 1980.0),
              ('boolean algebra', 1980.0),
              ('lazy propagation', 1980.0),
              ('palindrome algorithms', 1980.0),
              ('convex hull', 1980.0),
              ('sweep line', 1980.0),
              ('implementation', 2025.0),
              ('binary search', 2025.0),
              ('dynamic programming', 2250.0),
              ('breadth-first search', 2250.0),
              ('depth-first search', 2250.0),
              ('graph representation', 2250.0),
              ('hashing', 2250.0),
              ('bit manipulation', 2250.0),
              ('max flow', 2430.0),
              ('suffix trees', 2430.0),
              ('segment trees', 2700.0),
              ('fenwick trees', 2700.0),
              ('big data', 2700.0),
              ('unformatted input and output', 2700.0),
              ('file seeking', 2700.0),
              ('data compression', 2700.0),
              ('lexing and parsing', 2700.0),
              ('heuristics', 2700.0),
              ('genetic algorithms', 3150.0),
              ('particle swarm optimization', 3150.0)]
