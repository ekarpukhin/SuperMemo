import Card
import frontend
import constants
from random import choice
import pickle


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


def new_day(user):
    """
    main algorithm,
    :param user:
    :return:
    """
    print("Welcome back! It's day", user.day)
    cnt = 0
    with open('{}_cards.obj'.format(user.name), 'rb') as f:
        cards = pickle.load(f)
    for card in cards:
        if card.used == 1:
            if card.I == 1:
                sm2(card, frontend.question(card))
                cnt += 1
            else:
                card.I -= 1
    k = constants.batch_size - cnt
    if k > 0:
        for i in range(k):
            card = choice(cards)  # can pick used cards, need to fix
            sm2(card, frontend.question(card))
            card.used = 1

    open('{}_cards.obj'.format(user.name), 'wb').close()        #clearing cards file
    with open('{}_cards.obj'.format(user.name), 'wb') as f:     #writing changed cards
        pickle.dump(cards, f)

    user.day += 1
    open('{}.obj'.format(user.name), 'wb').close()  # clearing user file
    with open('{}.obj'.format(user.name), 'wb') as f:  # writing changed user info
        pickle.dump(user, f)

    print("Goodbye!")
    # the end of day
