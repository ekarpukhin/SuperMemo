import json
import time
from DataBase import Table
from reverso_context_api import Client


client = Client('en', 'ru')

cards_table = Table()
words_table = Table()
for i in range(8350, 8800, 50):
    words_table.cursor.execute(''' SELECT level, word from words where rowid >= ? and rowid < ?; ''', [i, i+50])
    words = words_table.cursor.fetchall()
    for word in words:
        card = [word[0], json.dumps({'question': word[1], 'answer': list(client.get_translations(word[1]))[:3]})]
        cards_table.cursor.execute(''' insert into cards(level, content) values(?, ?); ''', card)
        time.sleep(0.5)
    cards_table.connection.commit()
    print('successful from {} to {}'.format(i, i+50))



