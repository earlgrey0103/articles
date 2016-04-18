from collections import defaultdict
import json
import pprint


def tree():
    return defaultdict(tree)


def dicts(t):
    return {k: dicts(t[k]) for k in t}


def add(t, path):
    for node in path:
        t = t[node]


users = tree()
users['harold']['username'] = 'hrldcpr'
users['handler']['username'] = 'matthandlersux'

print(json.dumps(users))

taxonomy = tree()
taxonomy['Animalia']['Chordata']['Mammalia'][
    'Carnivora']['Felidae']['Felis']['cat']
taxonomy['Animalia']['Chordata']['Mammalia'][
    'Carnivora']['Felidae']['Panthera']['lion']
taxonomy['Animalia']['Chordata']['Mammalia'][
    'Carnivora']['Canidae']['Canis']['dog']
taxonomy['Animalia']['Chordata']['Mammalia'][
    'Carnivora']['Canidae']['Canis']['coyote']
taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['tomato']
taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['potato']
taxonomy['Plantae']['Solanales']['Convolvulaceae']['Ipomoea']['sweet potato']

add(taxonomy,
    'Animalia>Chordata>Mammalia>Cetacea>Balaenopteridae>Balaenoptera>blue whale'.split('>'))

pprint.pprint(dicts(taxonomy))
