from .global_vars import *
from .frontend import question
from .models import Users


def define_level(user: Users):
    """
    Defining level of user
    Default user level is 0
    :return: level
    """
    print('Lets define your level')
    for level in reversed(range(1, 7)):
        user.level = level
        if level_test(user, level):
            break


def level_test(user: Users, level):
    """
    User's given set of cards of certain level and he has to give answers.
    If his win rate will be good, return True
    :param level:
    :return bool
    """
    from .SuperMemo import TeachingIter
    print('level', level)
    correct = 0
    cards_iter = TeachingIter(test_size)
    # здесь надо в цикле брать карточку, отправлять пользователю, возвращать ответ, (ответ)/5 добавлять в correct
    # и вызывть process у итератора, отправляя ответ туда

    cards_iter.table.clear_user_cards()
    if correct / test_size >= min_win_rate:
        return 1
    return 0
