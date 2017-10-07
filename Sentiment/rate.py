import ReadFromFileTest as rfft
import json
import nltk
from collections import OrderedDict
import operator

datastore = OrderedDict()
with open("comments.json", 'r') as f:
    datastore = json.load(f)

for i in datastore.keys():
    sum = 0
    for j in datastore[i]:
        sum += rfft.rating(j)
    if (len(datastore[i]) != 0):
        datastore[i].insert(0,sum/len(datastore[i]))
    else:
        datastore[i].insert(0,-1)

datastore = sorted(datastore.items(), key=operator.itemgetter(1), reverse=True)

with open("sortedRating.json", 'w') as f:
    json.dump(datastore, f)
