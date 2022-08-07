from SuperMemo import TeachingIter
from DataBase import Table
from frontend import question

print('Hola, enter your name')
table = Table()
user = table.get_user(input())
teach = TeachingIter(user)
for card in teach:
    teach.process_card(question(card))

