import codeforcesApi
import json
from pprint import pprint

# 5 tags para empezar
easyTags = codeforcesApi.tagsRating[0:5]
problems = codeforcesApi.getProblemset(easyTags, 10)

for id, data in problems.items():
    data = codeforcesApi.getProblem(data)
    jsonData = json.dumps(data, indent=4)
    pprint(data)

    with open(f"problems/{id}.json", "w") as outfile:
        outfile.write(jsonData)
