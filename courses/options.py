from .models import *
from random import randint
from .define_accuracy import *

endings = ['а', 'я', 'о', 'у', 'ь', 'ы', 'ая', 'ое', 'ой', 'ые', 'ый', 'и', 'е', 'яя', 'ее', 'ие', 'йй']


def cut_ending(word: str):
    """
    Finds max possible ending in word and
    returns this word without maximal ending.
    """
    min_word = word
    for i in range(1, 3):
        if word[-i:] in endings:
            min_word = word[:-i]
    return min_word


OPTIONS = 5


def get_options(correct_word):
    options = []
    options_cnt = 0
    cutted_correct_word = cut_ending(correct_word)
    while options_cnt < OPTIONS:
        word_id = randint(1, 1_500_000)
        word = RussianWords.objects.get(id=word_id).word
        cutted_word = cut_ending(word)
        # print(word, cutted_word, cutted_correct_word)
        dist = 2 if len(word) < 6 else (len(word) // 2)
        if cutted_word != cutted_correct_word and \
                levenshtein(word, correct_word) < dist:
            options.append(word)
            options_cnt += 1
    return options
