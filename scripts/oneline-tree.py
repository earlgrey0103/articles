from collections import defaultdict
import json
import pprint


def tree(): return defaultdict(tree)


def dicts(t):
    return {k: dicts(t[k]) for k in t}


def add(t, path):
    for node in path:
        t = t[node]


users = tree()
users['codingpy']['username'] = 'earlgrey'
users['python']['username'] = 'Guido van Rossum'

print(json.dumps(users))

categories = tree()

categories['Programming Languages']['Python']
categories['Python']['Standard Library']['sys']
categories['Python']['Standard Library']['os']

print(json.dumps(categories))

pprint.pprint(dicts(categories))
