def question(card):
    """
    shows a card to user and returns whether he gave right answer or not
    :param: card: Card
    :return:
    """
    print(card.question)
    if input() in card.answer:
        print("you are right!")
        return 1
    print("wrong.")
    return 0
