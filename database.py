from reverso_context_api import Client
import pandas as pd
import random
import pickle

def f(x):
    try:
        return x[0]
    except BaseException:
        return 'huy'


client = Client('en', 'ru')

table = pd.read_csv('word_level.csv')
table.rename(columns={'a':'en', 'A1': 'level'}, inplace=True)
table['ru'] = 'что-то на русском'   # template, instead translated words
# table['ru'] = table['en'].map(client.get_translations)
# table['ru'] = table['ru'].map(list)
# table['ru'] = table['ru'].map(f)

tables = []

levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
for i in range(6):
    tables.append(table.loc[table.level == levels[i]])

with open('levels.obj', 'wb') as f:
    pickle.dump(tables, f)




