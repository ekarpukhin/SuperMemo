from .Card import Card
from .define_accuracy import define_accuracy


def grade(card: Card, user_answer):
    """
    Calls distance algorithm for all
    possible answers, print grade
    :param card:
    :param user_answer:
    :return: grade for best fit answer
    """
    num_grade = max(
        *map(
            lambda answer: define_accuracy(answer, user_answer), card.answer
        ), 0, 0
    )
    print(
        {
            0: "Dolboeb, incorrect",
            1: "Very Bad",
            2: "Very Bad, A few letters are correct",
            3: "Mediocre",
            4: "A few letters incorrect",
            5: "Excellent!"
        }[num_grade]
    )
    return num_grade


def question(card: Card):
    """
    shows a card to user,
    receive his answer and returns grade
    :param: card: Card
    :return:
    """
    print(card.question)
    user_answer = input()
    return grade(card, user_answer)


if __name__ == "__main__":
    print(question(Card('hello', [])))
