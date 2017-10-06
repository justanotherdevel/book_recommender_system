import ReadFromFileTest as rfft
import json
import nltk
from collections import OrderedDict
import operator

with open("comments.json", 'r') as f:
    datastore = json.load(f)

ratings = OrderedDict()
for i in datastore.keys():
    sum = 0
    for j in datastore[i]:
        sum += rfft.rating(j)
    if (len(datastore[i]) != 0):
        ratings[i] = sum/len(datastore[i])
sorted_ratings = OrderedDict()

sorted_ratings = sorted(ratings.items(), key=operator.itemgetter(1), reverse=True)
print (sorted_ratings)
