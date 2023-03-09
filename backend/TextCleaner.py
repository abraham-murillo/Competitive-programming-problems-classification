from string import punctuation
import unicodedata
from pylatexenc.latex2text import LatexNodes2Text

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

