from pprint import pprint

codeforcesToOmegaup = {
  "*special": [
    "big data",
    "file seeking",
    "data compression",
    "genetic algorithms",
    "particle swarm optimization"
  ],
  "2-sat": [
    "2-sat"
  ],
  "binary search": [
    "binary search"
  ],
  "bitmasks": [
    "bitmasks"
  ],
  "brute force": [
    "brute force"
  ],
  "chinese remainder theorem": [
    "chinese remainder theorem"
  ],
  "combinatorics": [
    "counting problems",
    "combinatorial designs",
    "numerical series",
    "combinations"
  ],
  "constructive algorithms": [
    "heuristics",
    "simulation",
    "incremental search",
    "exponential search",
    "nearest neighbors",
    "sweep line"
  ],
  "data structures": [
    "stacks",
    "queues",
    "segment trees",
    "fenwick trees",
    "monotone stack",
    "heaps",
    "wavelet trees",
    "linked lists",
    "tries",
    "offline queries",
    "sqrt decomposition",
    "lazy propagation"
  ],
  "dfs and similar": [
    "tree traversal",
    "recursion",
    "backtracking",
    "depth-first search",
    "depth first search"
  ],
  "divide and conquer": [
    "divide and conquer",
    "meet-in-the-middle"
  ],
  "dp": [
    "memorization",
    "recursion",
    "dynamic programming",
    "partial sums",
    "sub array search"
  ],
  "dsu": [
    "disjoint sets"
  ],
  "expression parsing": [
    "unformatted input and output",
    "lexing and parsing"
  ],
  "fft": [
    "fourier transformation"
  ],
  "flows": [
    "max flow"
  ],
  "games": [
    "game theory"
  ],
  "geometry": [
    "analytic geometry",
    "convex hull",
    "sweep line"
  ],
  "graph matchings": [
    "bipartite matching",
    "graph connectivity"
  ],
  "graphs": [
    "graph representation",
    "graph connectivity",
    "topological sorting",
    "directed graphs",
    "graphs with negative weights",
    "2-sat",
    "dfs and similar",
    "dsu",
    "flows",
    "graph matchings",
    "shortest paths",
    "trees"
  ],
  "greedy": [
    "greedy algorithms",
    "schedules"
  ],
  "hashing": [
    "hashing"
  ],
  "implementation": [
    "formatted input and output",
    "functions",
    "loops",
    "conditionals",
    "input and output",
    "arrays",
    "implementation",
    "heuristics",
    "simulation",
    "inverted indices",
    "incremental search",
    "local search",
    "sub array search",
    "subsequence search",
    "offline queries"
  ],
  "math": [
    "boolean algebra",
    "arithmetic",
    "modular arithmetic",
    "analysis of recurrences",
    "big numbers",
    "bit manipulation",
    "exponentiation by squaring",
    "systems of equations",
    "diophantine equations",
    "modular multiplicative inverse",
    "permutations",
    "2-sat",
    "matrices"
  ],
  "matrices": [
    "matrices"
  ],
  "meet-in-the-middle": [
    "meet in the middle"
  ],
  "number theory": [
    "number theory",
    "common multiples and divisors",
    "primality test",
    "prime generation",
    "prime factorization",
    "divisibility rules",
    "modular multiplicative inverse",
    "chinese remainder theorem"
  ],
  "probabilities": [
    "probability and statistics"
  ],
  "schedules": [
    "schedules"
  ],
  "shortest paths": [
    "breadth-first search",
    "breadth first search",
    "shortest paths"
  ],
  "sortings": [
    "sorting"
  ],
  "string suffix structures": [
    "string matching",
    "tries",
    "palindrome algorithms",
    "suffix trees"
  ],
  "strings": [
    "chars and strings",
    "string matching",
    "tries",
    "palindrome algorithms",
    "string suffix structures"
  ],
  "ternary search": [
    "ternary search"
  ],
  "trees": [
    "binary search tree",
    "minimum spanning trees",
    "trees",
    "least common ancestor"
  ],
  "two pointers": [
    "sliding window",
    "two pointers technique"
  ]
}

omegaupToCodeforces = {
  '2-sat': ['2-sat', 'graphs', 'math'],
  'analysis of recurrences': ['math'],
  'analytic geometry': ['geometry'],
  'arithmetic': ['math'],
  'arrays': ['implementation'],
  'backtracking': ['dfs and similar'],
  'big data': ['*special'],
  'big numbers': ['math'],
  'binary search': ['binary search'],
  'binary search tree': ['trees'],
  'bipartite matching': ['graph matchings'],
  'bit manipulation': ['math'],
  'bitmasks': ['bitmasks'],
  'boolean algebra': ['math'],
  'breadth first search': ['shortest paths'],
  'breadth-first search': ['shortest paths'],
  'brute force': ['brute force'],
  'chars and strings': ['strings'],
  'chinese remainder theorem': ['chinese remainder theorem', 'number theory'],
  'combinations': ['combinatorics'],
  'combinatorial designs': ['combinatorics'],
  'common multiples and divisors': ['number theory'],
  'conditionals': ['implementation'],
  'convex hull': ['geometry'],
  'counting problems': ['combinatorics'],
  'data compression': ['*special'],
  'depth first search': ['dfs and similar'],
  'depth-first search': ['dfs and similar'],
  'dfs and similar': ['graphs'],
  'diophantine equations': ['math'],
  'directed graphs': ['graphs'],
  'disjoint sets': ['dsu'],
  'divide and conquer': ['divide and conquer'],
  'divisibility rules': ['number theory'],
  'dsu': ['graphs'],
  'dynamic programming': ['dp'],
  'exponential search': ['constructive algorithms'],
  'exponentiation by squaring': ['math'],
  'fenwick trees': ['data structures'],
  'file seeking': ['*special'],
  'flows': ['graphs'],
  'formatted input and output': ['implementation'],
  'fourier transformation': ['fft'],
  'functions': ['implementation'],
  'game theory': ['games'],
  'genetic algorithms': ['*special'],
  'graph connectivity': ['graph matchings', 'graphs'],
  'graph matchings': ['graphs'],
  'graph representation': ['graphs'],
  'graphs with negative weights': ['graphs'],
  'greedy algorithms': ['greedy'],
  'hashing': ['hashing'],
  'heaps': ['data structures'],
  'heuristics': ['constructive algorithms', 'implementation'],
  'implementation': ['implementation'],
  'incremental search': ['constructive algorithms', 'implementation'],
  'input and output': ['implementation'],
  'inverted indices': ['implementation'],
  'lazy propagation': ['data structures'],
  'least common ancestor': ['trees'],
  'lexing and parsing': ['expression parsing'],
  'linked lists': ['data structures'],
  'local search': ['implementation'],
  'loops': ['implementation'],
  'matrices': ['math', 'matrices'],
  'max flow': ['flows'],
  'meet in the middle': ['meet-in-the-middle'],
  'meet-in-the-middle': ['divide and conquer'],
  'memorization': ['dp'],
  'minimum spanning trees': ['trees'],
  'modular arithmetic': ['math'],
  'modular multiplicative inverse': ['math', 'number theory'],
  'monotone stack': ['data structures'],
  'nearest neighbors': ['constructive algorithms'],
  'number theory': ['number theory'],
  'numerical series': ['combinatorics'],
  'offline queries': ['data structures', 'implementation'],
  'palindrome algorithms': ['string suffix structures', 'strings'],
  'partial sums': ['dp'],
  'particle swarm optimization': ['*special'],
  'permutations': ['math'],
  'primality test': ['number theory'],
  'prime factorization': ['number theory'],
  'prime generation': ['number theory'],
  'probability and statistics': ['probabilities'],
  'queues': ['data structures'],
  'recursion': ['dfs and similar', 'dp'],
  'schedules': ['greedy', 'schedules'],
  'segment trees': ['data structures'],
  'shortest paths': ['graphs', 'shortest paths'],
  'simulation': ['constructive algorithms', 'implementation'],
  'sliding window': ['two pointers'],
  'sorting': ['sortings'],
  'sqrt decomposition': ['data structures'],
  'stacks': ['data structures'],
  'string matching': ['string suffix structures', 'strings'],
  'string suffix structures': ['strings'],
  'sub array search': ['dp', 'implementation'],
  'subsequence search': ['implementation'],
  'suffix trees': ['string suffix structures'],
  'sweep line': ['constructive algorithms', 'geometry'],
  'systems of equations': ['math'],
  'ternary search': ['ternary search'],
  'topological sorting': ['graphs'],
  'tree traversal': ['dfs and similar'],
  'trees': ['graphs', 'trees'],
  'tries': ['data structures', 'string suffix structures', 'strings'],
  'two pointers technique': ['two pointers'],
  'unformatted input and output': ['expression parsing'],
  'wavelet trees': ['data structures']
}

def getOmegaupTopics(topic):
  if topic in codeforcesToOmegaup:
    return codeforcesToOmegaup[topic]
  return []

# def getInverse():
#   inv = dict()
#   for codeforces, omegaupList in codeforcesToOmegaup.items():
#     for omegaup in omegaupList:
#       if omegaup not in inv:
#         inv[omegaup] = [codeforces]
#       else:
#         inv[omegaup].append(codeforces)
#   pprint(inv)

def getCodeforcesTopics(topic):
  if topic in omegaupToCodeforces:
    return omegaupToCodeforces[topic]
  return []

  