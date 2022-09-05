from Levenshtein import ratio

#
# def levenshtein(a: str, b: str):
#     """
#     Our not working version of Levenshtein algorithm!!!
#
#     Calculates the Levenshtein distance between a and b
#     :param a: Right string
#     :param b: User's answer
#     :return: distance between strings()
#     """
#     n, m = len(a), len(b)
#     if n > m:
#         # Make sure n <= m, to use O(min(n, m)) space
#         a, b = b, a
#         n, m = m, n
#
#     current_row = np.arange(0, n + 1)
#     # previous_row = np.arange(0, n + 1)
#     # current_row = [0] * (n + 1)
#     # previous_row = [0] * (n + 1)
#     for i in range(1, m + 1):
#         previous_row = np.copy(current_row)
#         current_row.fill(0)
#         current_row[0] = i
#         # print(previous_row,  current_row, end="\n")
#
#         for j in range(1, n + 1):
#             change = previous_row[j - 1]
#             if a[j - 1] != b[i - 1]:
#                 change += 1
#             # add, delete, change
#             current_row[j] = min(previous_row[j] + 1, current_row[j - 1] + 1, change)
#         # print(previous_row,  current_row, end="\n\n")
#     return current_row[n]


def levenshtein(a: str, b: str):
    """
    Not use!!!

    Calculates the Levenshtein distance between a and b
    :param a: Right string
    :param b: User's answer
    :return: distance between strings()
    """
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n, m)) space
        a, b = b, a
        n, m = m, n

    current_row = [0] * (n + 1)
    previous_row = [0] * (n + 1)
    for i in range(1, m + 1):
        for _i in range(n + 1):
            previous_row[_i] = current_row[_i]
            current_row[_i] = 0
        current_row[0] = i
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + \
                1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]


def define_accuracy(correct_answer, user_answer):
    distance = ratio(correct_answer, user_answer)
    error_rate = distance / len(user_answer)
    if error_rate > 0.5 and distance > 4:
        return 0
    if error_rate > 0.4 and distance > 3:
        return 1
    if error_rate > 0.3 and distance > 2:
        return 2
    if error_rate > 0.2 and distance > 0:
        return 3
    if error_rate > 0 and distance > 0:
        return 4
    if error_rate == 0:
        return 5
