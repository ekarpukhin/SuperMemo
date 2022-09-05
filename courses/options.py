from .models import *
from random import randint, choice, sample
from .define_accuracy import *
from Levenshtein import ratio

import time

endings = {1: ['а', 'я', 'о', 'е', 'ы', 'и', 'а', 'я', 'у', 'ю'],
           2: ['ой', 'ая', 'яя', 'ое', 'ее',
               'ов', 'ев', 'ых', 'их', 'ам', 'ям',
               'ому', 'ему', 'ий', 'ый', 'ую', 'юю',
               'ей', 'ые', 'ие', 'ом', 'ем',
               'им', 'ым', 'ах', 'ях', ],
           3: ['ыми', 'ими', 'ами', 'ями', 'ого', 'его', ]}


def cut_ending(word: str):
    """
    Finds max possible ending in word and
    returns this word without maximal ending.
    """
    min_word = word
    for i in range(1, 3):
        if word[-i:] in endings[i]:
            min_word = word[:-i]
    return min_word


OPTIONS = 5


def get_options(correct_word_list):
    global_start_time = time.time()

    options = []
    correct_dict = {correct_word: cut_ending(correct_word) for correct_word in correct_word_list}
    query_set = RussianWords.objects.order_by('?')
    # query_set = RussianWords.objects.all()
    lev_times = []
    for line in query_set.iterator():
        word = line.word
        cut_word = line.cut
        for i in range(3):
            correct_word, cut_correct_word = list(correct_dict.items())[i]
            dist = 2 if len(word) < 6 else (len(word) // 2)
            lev_time = time.time()
            if cut_word != cut_correct_word and \
                    ratio(word, correct_word) < dist:
                options.append(word)
            lev_times.append(time.time()-lev_time)

        if len(options) > 4:
            break

    print(len(options))
    print("searching time: {}\nleven time: {}".format(time.time() - global_start_time,
                                                      sum(lev_times)))
    return sample(options, OPTIONS)
