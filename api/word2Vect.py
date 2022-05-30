import linecache
from pprint import pprint

trash = "trash.txt"
# word2VecEnglish = open("Word2VecEnglish.txt", "r")
# word2VecEnglishSortedWords = "api/Word2VecEnglishSortedWords.txt"
# Word2VectEnglishSorted = "api/Word2VecEnglishSorted.txt"

# TODO: Make if read from files

def getVector(word):

    # lo = 0
    # hi =
    # while lo + 1 < hi:
    #     mid = (lo + hi) // 2
    #     midWord = linecache.getline(word2VecEnglishSortedWords, mid)
    #     if word < midWord:
    #         hi = mid
    #     else:
    #         lo = mid

    # return lo if linecache.getline(word2VecEnglishSortedWords, lo) == word else hi


getVector("hello")
