import constants
import numpy
from database import tables

class User:
    def __init__(self, name):
        self.name = name
        self.level = define_level()
        self.batch = create_batch(self.level)
        self.day


def define_level():
    """
    Defining level of user
    Default user level is 3
    :return:
    """
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

    win_rate = 0
    i = 0
    cards = tables[level]
    while i < constants.test_size:
        if answer(tables[level].sample(1)['en']):
            win_rate += 1
    if win_rate > constants.win_rate:
        return 1
    return 0

rand = numpy.random.choice(tables[0])
print(rand)

