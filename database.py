from reverso_context_api import Client
import pandas as pd
import random

def huy(x):
    try:
        return x[0]
    except BaseException:
        return 'huy'


client = Client('en', 'ru')

table = pd.read_csv('word_level.csv').head(50)
table.rename(columns={'a':'en', 'A1': 'level'}, inplace=True)
table['ru'] = table['en'].map(client.get_translations)
table['ru'] = table['ru'].map(list)
try:
    table['ru'] = table['ru'].map(huy)
except BaseException:
    pass

tables = []

levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
for i in range(6):
    tables.append(table.loc[table.level == levels[i]])

print(tables[0])

rand = tables[0].sample(4)['en']
print(rand)
