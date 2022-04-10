import copy
import constants
from database import tables
from random import choice
import pickle
import frontend

class User:
    def __init__(self, name):
        self.name = name
        self.level = define_level()
        self.day = 1
        create_batch(self.level, self.name)


def define_level():
    """
    Defining level of user
    Default user level is 0
    :return:
    """
    print('Lets define your level')
    for level in range(5, 0, -1):
        if level_test(level):
            return level
    return 0


def level_test(level):
    """
    User's given set of cards of certain level and he has to give answers.
    If his win rate will be good and batch will be filled, return batch of cards.
    :param level:
    :return: batch of cards if it's user's level and 0 if not
    """
    print('level', level)
    win_rate = 0
    i = 0
    with open('cards.obj', 'rb') as f:
        cards = pickle.load(f)[level]
    while i < constants.test_size:
        if frontend.question(choice(cards)):
            win_rate += 1
        i += 1
    if win_rate > constants.win_rate:
        return 1
    return 0


def create_batch(level, name):
    with open('cards.obj', 'rb') as f:
        cards = (pickle.load(f))[level]
    user_cards = []
    for card in cards:
        user_cards.append(copy.deepcopy(card))
    with open('{}_cards.obj'.format(name), 'wb') as f:
        pickle.dump(user_cards, f)

