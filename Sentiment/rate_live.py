#!/usr/bin/env python
import ReadFromFileTest as rfft
import json
import nltk
from collections import OrderedDict
import operator

def nProcess():
    datastore = dict()
    with open("/home/shashwat/Programs/Python/book_recommender_system/Sentiment/comments.json", 'r') as f:
        datastore = json.load(f)
        data = dict()
    
    for i in datastore.keys():
        sum = 0
        for j in datastore[i]:
            sum += rfft.rating(j)
        if (len(datastore[i]) != 0):
            data[i] = sum/len(datastore[i])
    
    data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    
    with open("/home/shashwat/Programs/Python/book_recommender_system/Sentiment/sortedRating.json", 'w') as f:
        json.dump(data, f, indent=4) 
    
    print ("Success")

if __name__=="__main__":
    nProcess()
