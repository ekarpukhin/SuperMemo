from .User import User
from .Card import Card
from .global_vars import *
from .DataBase import Table


def sm2(card: Card, q: bool):
    """
    Main algorithm, modifies only
    cards with interval I=1.
    :param card:
    :param q:
    :return:
    """
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
    card.EF += 0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)
    if card.EF < 1.3:
        card.EF = 1.3


class TeachingIter:
    """
    Iterator, that returns Card objects
    from user's card set and
    receiving requests.
    """
    def __init__(self, user: User, card_set_size=batch_size):
        self.user = user
        self.table = Table(user)
        self.get_card = self.table.get_cards()
        self.used_cnt = 0
        self.curr_card = None
        self.used_cards = []
        self.card_set_size = card_set_size

    def process_card(self, ans):
        """
        Processing last card that was given to user
        and update it in the user's card set.
        :param ans:
        :return:
        """
        sm2(self.curr_card, ans)
        self.table.update_card(self.curr_card)
        self.used_cnt += 1

    def __iter__(self):
        return self

    def __next__(self):
        """
        Gives cards that already was given ago till
        they exist, then load new cards and repeats till
        number of given cards less then number of cards per day.
        :return: card: Card
        """
        if self.used_cnt >= self.card_set_size:
            raise StopIteration
        while True:
            try:
                card = next(self.get_card)
            except StopIteration:
                self.table.used_size = self.used_cnt
                self.table.load_random_cards()
                self.get_card = self.table.get_cards()
            else:
                print([card.question for card in self.used_cards])
                if card not in self.used_cards:
                    self.used_cards.append(card)
                    if card.I == 1:
                        self.curr_card = card
                        return card
                    card.I -= 1
                    self.table.update_card(card)
