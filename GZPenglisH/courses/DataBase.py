import json
from .Card import Card
from .User import User
from .global_vars import batch_size
from django.db import connection


class Table:
    def __init__(self, user=None):
        """
        Create connection if not exist and some fields
        to make queries.
        :param user:
        """
        self.user = user
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.last_card_id = None
        self.used_size = 0

    def get_user(self, name):
        """
        If user with this name exists, return
        User obj based on user table. Else, create new
        user and write it to user table.
        :param name:
        :return:
        """
        self.cursor.execute(''' select id, name, level from users where name = %s ''', [name])
        user_data = self.cursor.fetchall()
        if user_data:
            self.user = User(*user_data[0])
            return self.user
        self.cursor.execute(''' select count(*) from users ''')
        new_user_id = self.cursor.fetchall()[0][0] + 1
        self.user = User(new_user_id, name)
        self.cursor.execute(''' INSERT INTO users(name, level) VALUES (%s, %s); ''',
                            [self.user.name, self.user.level])
        self.connection.commit()
        return self.user

    def load_random_cards(self):
        """
        It usually called when used cards run out.
        Selecting cards in cards table whose id is not
        the id that current user's card have. Then load them to
        user's card set.
        :return:
        """
        self.cursor.execute(''' SELECT id FROM cards
            where level = %s and ROWID < 8800 and id not in 
            (
                select card_id_id from cards_info where user_id_id = %s
            )       
            ORDER BY random() LIMIT %s; ''', [self.user.level, self.user.id, batch_size - self.used_size])
        cards = self.cursor.fetchall()
        for card in cards:
            card_id = card[0]
            self.cursor.execute(
                ''' INSERT INTO cards_info(card_id_id, user_id_id) values (%s, %s)''', [card_id, self.user.id])
        self.connection.commit()

    def get_cards(self):
        """
        Generator function, return Cards that are in
        user's card set and change last card id(it's for update_card function).
        :return:
        """
        self.cursor.execute(''' SELECT content, card_info, card_id_id FROM cards_info a
        left join cards b on b.id = a.card_id_id WHERE user_id_id = %s
                 ORDER BY random(); ''', [self.user.id])
        cards = self.cursor.fetchall()
        for card in cards:
            new_card = card_from_json(card[0], card[1])
            self.last_card_id = card[2]
            yield new_card

    def update_card(self, card: Card):
        """
        Updates last card given outside.
        :param card:
        :return:
        """
        self.cursor.execute(''' UPDATE cards_info
                                SET card_info = %s
                                WHERE card_id_id = %s and user_id_id ; ''',
                            [json_from_card(card), self.last_card_id])
        self.connection.commit()

    def clear_user_cards(self):
        """
        Usually need after level tests.
        :return:
        """
        self.cursor.execute('''DELETE FROM cards_info where user_id_id = %s''', [self.user.id])
        self.connection.commit()


def json_from_card(card: Card):
    d = card.__dict__.copy()
    d.pop('question')
    d.pop('answer')
    return json.dumps(d)


def card_from_json(content, info=None):
    d1 = json.loads(content)
    if not info:
        return Card(d1['question'], d1['answer'])
    d2 = json.loads(info)
    return Card(d1['question'], d1['answer'], d2['I'], d2['n'], d2['EF'])

