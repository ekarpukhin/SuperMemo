import pickle
import pandas as pd

class Card:
    def __init__(self, question, answer):
        self.I = 0
        self.n = 0
        self.EF = 2.5
        self.question = question
        self.answer = answer
        self.used = 0


cards = [[] for i in range(6)]
with open('levels.obj', 'rb') as f:
    levels = pickle.load(f)

for level, card in zip(levels, cards):
    for index, row in level.iterrows():
        card.append(Card(row['en'], row['ru']))

with open('cards.obj', 'wb') as f:
    pickle.dump(cards, f)



