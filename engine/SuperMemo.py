import frontend
import User
from Card import Card
import global_vars
from DataBase import Table


def sm2(card: Card, q):
    q *= 5
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
    def __init__(self, user: User):
        self.user = user
        self.table = Table(user)
        self.get_card = self.table.get_cards()
        self.used_cnt = 0
        self.curr_card = None

    def process_card(self, ans: bool):
        sm2(self.curr_card, ans)
        self.table.update_card(self.curr_card)
        self.used_cnt += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.used_cnt >= global_vars.batch_size:
            raise StopIteration
        while True:
            try:
                card = next(self.get_card)
            except StopIteration:
                self.table.used_size = self.used_cnt
                self.table.load_random_cards()
                self.get_card = self.table.get_cards()
            else:
                if card.I == 1:
                    self.curr_card = card
                    return card
                card.I -= 1
                self.table.update_card(card)
