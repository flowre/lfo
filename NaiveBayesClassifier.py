__author__ = 'liamgeron'
from collections import Counter
import nltk
# See more at NLTK Chapter 6
# P(label|features) = P(features, label)/P(features)
# P(features) is constant for each label, so it suffices to calculate P(features, label)
# P(features, label) = P(label) x P(features|label)
class NaiveBayes:
    def __init__(self):
        self.probabilities = {}

    # Takes a training file in the format of a tuple with (word, label)
    def train(self, trainingFile):
        # Enumerate creates a tuple from a list of (index, item)
        # Featureset is a tuple with ({features}, label)
        # Should train with featureset by calculating probability for each feature given label
        label_freqdist = nltk.FreqDist()
        features = [f for f in trainingFile[0][0]]
        f_counts = {}
        for f in features:
            for t in trainingFile:
                if t[0][f] ==
                f_counts[f]





def feature_extract(sent, i):
    # Extract features of interest where sent is observed states and i is the index
    features = {}

    return features

featuresets = []
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]