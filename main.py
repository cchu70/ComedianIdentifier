import nltk
import csv
from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation
import random
data = []

def tokenize_raw_data(raw_data):
    tokenized = []
    for row in raw_data:
        tokenized.append([row[0], row[1], row[2], word_tokenize(row[3])])
    return tokenized

with open('Final CSV  - Sheet1.csv') as file:
        reader = csv.reader(file, delimiter=',')
        line = 0
        for row in reader:
            if line != 0:
                data.append(row)
            line += 1
tokenized_data = tokenize_raw_data(data)
total = 0
for counter in range(100):
    random.shuffle(tokenized_data)
    feature_sets = []
    for i in tokenized_data:
        word_feature = dict([(word.lower(), True) for word in i[3] if word not in punctuation and word.lower not in ['trump', 'laughter', 'cheering', 'applause']])
        feature_sets.append((word_feature, i[0]))

    training_set = feature_sets[:50]
    testing_set= feature_sets[50:]
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    total += (nltk.classify.accuracy(classifier, testing_set))*100
print("Classifier accuracy percent:", total/100.0)