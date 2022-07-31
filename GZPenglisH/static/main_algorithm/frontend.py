def question(card):
    """
    shows a card to user and returns whether he gave right answer or not
    :param: card: Card
    :return:
    """
    print(card.question)
    if input() == card.answer:
        return 1
    return 0