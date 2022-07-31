from database import tables
import pa


def create_batch(level):
    """
    creating set of card for certain level by adding cards that user don't know
    :param: level
    :return: batch of cards
    """

    batch = []
    cnt = 0
    while cnt <= batch_size:
        card = cards[]
        if not answer(cards[]):
            batch.append(card)