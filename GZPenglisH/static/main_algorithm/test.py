from frontend import question
import Card
import pickle
import User
import SuperMemo

#
# with open('cards.obj', 'rb') as f:
#     card = (pickle.load(f))[1][5]
#
# print(question(card))

print('print your name: ', end='')
name = input()
print('print how many days you wanna study')
n = int(input())
try:
    f = open('{}.obj'.format(name), 'rb')
    user = pickle.load(f)
except IOError:
    user1 = User.User(name)
    with open('{}.obj'.format(name), 'wb') as f:
        pickle.dump(user1, f)
    with open('{}.obj'.format(name), 'rb') as f:
        user = pickle.load(f)

print("Name:", user.name, "level:", user.level, "day:", user.day)
for i in range(n):
    SuperMemo.new_day(user)
print("Name:", user.name, "level:", user.level, "day:", user.day)

# что-то на русском
