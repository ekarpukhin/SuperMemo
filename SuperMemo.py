# Constants
batch_size = 50

class Card:
    def __init__(self, question, answer):
        self.I = 0
        self.n = 0
        self.EF = 2.5
        self.question = question
        self.answer = answer
        self.used = 0


cards = {}


def sm2(card: Card, q):
    if q >= 3:
        if card.n == 0:
            card.I = 1
        elif card.n == 1:
            card.I = 6
        else:
            card.I = round(card.I * card.EF)
        card.n += 1
    else:
        card.n = 0
        card.I = 1
    card.EF += 0.1 - (5 - q)*(0.08 + (5 - q)*0.02)
    if card.EF < 1.3:
        card.EF = 1.3

def get_card():







