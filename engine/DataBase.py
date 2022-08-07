import sqlite3
from sqlite3 import Error
import json
from Card import Card
from User import User
from global_vars import batch_size


class DataBase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        try:
            self.connection = sqlite3.connect('DataBase')
            print('Connection Succeeded')
        except Error:
            print('Ooops, somth wrong')

    def __del__(self):
        self.connection.close()


class Table:
    def __init__(self, user=None):
        self.user = user
        db = DataBase()
        self.connection = db.connection
        self.cursor = self.connection.cursor()
        self.last_card_id = None
        self.used_size = 0

    def get_user(self, name):
        self.cursor.execute(''' select id, name, level from users where name = ?''', [name])
        user_data = self.cursor.fetchall()
        if user_data:
            self.user = User(*user_data[0])
            return self.user
        self.cursor.execute(''' select count(*) from users ''')
        new_user_id = self.cursor.fetchall()[0][0] + 1
        self.user = User(new_user_id, name)
        self.cursor.execute(''' INSERT INTO users(name, level) VALUES (?, ?); ''',
                            [self.user.name, self.user.level])
        self.connection.commit()
        return self.user

    def load_random_cards(self):
        self.cursor.execute(''' SELECT id FROM cards
            where level = ? and ROWID < 8800 and id not in 
            (
                select card_id from cards_info where user_id = ?
            )       
            ORDER BY random() LIMIT ?; ''', [self.user.level, self.user.id, batch_size - self.used_size])
        cards = self.cursor.fetchall()
        for card in cards:
            card_id = card[0]
            self.cursor.execute(
                ''' INSERT INTO cards_info(card_id, user_id) values (?, ?)''', [card_id, self.user.id])
        self.connection.commit()

    def get_cards(self):    # smth wrong with join
        self.cursor.execute(''' SELECT content, info, card_id FROM cards_info a
        left join cards b on b.id = a.card_id WHERE user_id = ?
                 ORDER BY random(); ''', [self.user.id])
        cards = self.cursor.fetchall()
        for card in cards:
            new_card = card_from_json(card[0], card[1])
            self.last_card_id = card[2]
            yield new_card

    def update_card(self, card: Card):
        self.cursor.execute(''' UPDATE cards_info
                                SET info = ?
                                WHERE card_id = ? and user_id ; ''',
                            [json_from_card(card), self.last_card_id])
        self.connection.commit()

    def clear_user_cards(self):
        self.cursor.execute('''DELETE FROM cards_info where user_id = ?''', [self.user.id])


def json_from_card(card: Card):
    d = card.__dict__.copy()
    d.pop('question')
    d.pop('answer')
    return json.dumps(d)


def card_from_json(contain, info=None):
    d1 = json.loads(contain)
    if not info:
        return Card(d1['question'], d1['answer'])
    d2 = json.loads(info)
    return Card(d1['question'], d1['answer'], d2['I'], d2['n'], d2['EF'])
