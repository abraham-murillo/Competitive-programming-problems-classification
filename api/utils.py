"""
Collection of functions to make life easier
"""


def topicsForReact(topics):
    """
    {id, name} pair is needed for component <ReactTags/>
    """
    return [{"id": topic, "name": topic} for topic in topics]


def getProblemId(url):
    """
    Returns problem id used in firebase
    """
    id = ""
    url = url.split("/")
    if "omegaup.com" in url:
        id = f"omegaup-{url[-1]}"
    elif "codeforces.com" in url:
        id = f"codeforces-{url[-2]}{url[-1]}"
    return id
