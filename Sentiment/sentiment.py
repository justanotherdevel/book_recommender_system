import nltk
import random
import pickle
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
from nltk.classify import accuracy

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

save_documents = open ("pickle/documents.pickle","wb")
pickle.dump(documents, save_documents)
save_documents.close()

random.shuffle(documents)

entire_word_list = []

for w in movie_reviews.words():
    entire_word_list.append(w.lower())

# Arrange the list in decreasing order of the frequency
entire_word_list = nltk.FreqDist(entire_word_list)

features = list (entire_word_list.keys())[:3000]

save_features = open ("pickle/features.pickle","wb")
pickle.dump(features, save_features)
save_features.close()

def find_features(document):
    words = set(document)
    gen_features = {}
    for w in features:
        gen_features[w] = (w in words)
    return gen_features

featureset = [(find_features(rev), category) for (rev, category) in documents]

no_of_test_elements = 1900
training_set = featureset[:no_of_test_elements]
testing_set = featureset [no_of_test_elements:]

classifier = nltk.NaiveBayesClassifier.train (training_set)
print ("Accuracy of nlkt NaiveBayes: ", (accuracy(classifier, testing_set))*100)

save_classifier = open ("pickle/oNaiveBayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

mNB = SklearnClassifier (MultinomialNB())
mNB.train(training_set)
print ("Accurace of mNB: ", (accuracy(mNB, testing_set)*100))

save_classifier = open ("pickle/mNB.pickle","wb")
pickle.dump(mNB, save_classifier)
save_classifier.close()

bNB = SklearnClassifier (BernoulliNB())
bNB.train(training_set)
print ("Accurace of bNB: ", (accuracy(bNB, testing_set)*100))

save_classifier = open ("pickle/bNB.pickle","wb")
pickle.dump(bNB, save_classifier)
save_classifier.close()

LogisticRegression = SklearnClassifier (LogisticRegression())
LogisticRegression.train(training_set)
print ("Accurace of LogisticRegression: ", (accuracy(LogisticRegression, testing_set)*100))

save_classifier = open ("pickle/LogisticRegression.pickle","wb")
pickle.dump(LogisticRegression, save_classifier)
save_classifier.close()

SGDC = SklearnClassifier (SGDClassifier())
SGDC.train(training_set)
print ("Accurace of SGDClassifier: ", (accuracy(SGDC, testing_set)*100))

save_classifier = open ("pickle/SGDC.pickle","wb")
pickle.dump(SGDC, save_classifier)
save_classifier.close()
