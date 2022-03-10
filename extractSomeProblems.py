import codeforces
import json
import pprint

# 5 tags para empezar
easyTags = codeforces.tagsRating[0:5]
problems = codeforces.getProblemset(easyTags, 10)

for id, data in problems.items():
    data = codeforces.getProblem(data)
    jsonData = json.dumps(data, indent=4)
    pprint.pprint(data)

    with open(f"problems/{id}.json", "w") as outfile:
        outfile.write(jsonData)
