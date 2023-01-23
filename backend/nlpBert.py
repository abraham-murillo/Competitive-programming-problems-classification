# https://pytorch.org/get-started/locally/

from transformers import BertTokenizer, BertModel, BertForSequenceClassification

import torch
import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
import json

from extractSomeProblems import startingTopics

def getAllProblems():
  problems = []
  for topic in startingTopics:
    codeforcesProblems = json.load(open(f"data/codeforces-{topic}.json"))
    problems.extend(codeforcesProblems)
    # omegaupProblems = json.load(open(f"data/omegaup-{topic}.json"))
    # problems.extend(omegaupProblems)

  return problems

# pprint(len(getAllProblems()))
# pprint(getAllProblems()[-1])

problems = getAllProblems()

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained("bert-base-uncased")

text = problems[-1]['history']
encodedInput = tokenizer(text, return_tensors='pt')
# result = model(encodedInput)

# pprint(result.logits)