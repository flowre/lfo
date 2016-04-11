__author__ = 'liamgeron'
import nltk
import random
from numpy.random import choice

class MarkovChain:
    def __init__(self):
        self.transitionMatrix = {}

    def train(self,states):
        self.states = states
        fdist = nltk.FreqDist(states)
        cfd = nltk.ConditionalFreqDist(nltk.bigrams(states))
        for s in states:
            self.transitionMatrix[s] = {}
            for a in states:
                self.transitionMatrix[s][a] = cfd[s][a] / fdist[s]

    # Get some start probabilities and instigate a sentence with them
    # Should implement some triple based generation
    # incorporate random choice using numpy, that'll end the infinite loop
    def generate(self, length):
        # Should do seed = random.randint(0,len(self.states))
        # seed, next = self.states[seed], self.states[seed+1]
        # Gets first bigram
        seed = self.states[random.randint(0,len(self.states))]
        l = 1
        generated_states = []
        generated_states.append(seed)
        while l <= length:
            seed = choice((list(self.transitionMatrix[seed].keys())), 1, list(self.transitionMatrix[seed].values()))
            print(seed)
            l += 1
        return ' '.join(generated_states)

training_set = nltk.corpus.brown.words(categories='news')[:100]
training_set = [w.lower() for w in training_set]
mc = MarkovChain()
mc.train(training_set)
mc.generate(12)