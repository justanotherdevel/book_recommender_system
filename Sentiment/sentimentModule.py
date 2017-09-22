import nltk
import random
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize

class AggClassifier (ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify (self, features):
        aggregate = []
        for c in self._classifiers:
            a = c.classify (features)
            aggregate.append(a)
        return mode(aggregate)

    def correctness (self, features):
        aggregate = []
        for c in self._classifiers:
            a = c.classify (features)
            aggregate.append(a)
        return aggregate.count(mode(aggregate))/len(aggregate)

documents_read = open("pickle/documents.pickle", "rb")
documents = pickle.load(documents_read)
documents_read.close()

features_read = open("pickle/features.pickle", "rb")
features = pickle.load(features_read)
features_read.close()

def find_features(document):
    words = set(document)
    gen_features = {}
    for w in features:
        gen_features[w] = (w in words)
    return gen_features

open_file = open("pickle/oNaiveBayes.pickle", "rb")
classifier = pickle.load(open_file)
open_file.close()

open_file = open("pickle/bNB.pickle", "rb")
bNB = pickle.load(open_file)
open_file.close()

open_file = open("pickle/mNB.pickle", "rb")
mNB = pickle.load(open_file)
open_file.close()

open_file = open("pickle/SGDC.pickle", "rb")
SGDC = pickle.load(open_file)
open_file.close()

open_file = open("pickle/LogisticRegression.pickle", "rb")
LogisticRegression = pickle.load(open_file)
open_file.close()

aggregate_classifier = AggClassifier(
        classifier,
        bNB,
        mNB,
        SGDC,
        LogisticRegression)

def sentiment (text):
    feats = find_features(text)
    return aggregate_classifier.classify(feats), aggregate_classifier.correctness(feats)
