import global_vars
import frontend


class User:
    def __init__(self, id, name, level=None):
        self.name = name
        self.id = id
        if not level:
            self.define_level()
        else:
            self.level = level

    def define_level(self):
        """
        Defining level of user
        Default user level is 0
        :return: level
        """
        print('Lets define your level')
        for level in reversed(range(1, 6)):
            self.level = level
            if self.level_test(level):
                break

    def level_test(self, level):
        """
        User's given set of cards of certain level and he has to give answers.
        If his win rate will be good, return True
        :param level:
        :return bool
        """
        from DataBase import Table
        print('level', level)
        correct = 0
        table = Table(self)
        table.load_random_cards()
        cards = table.get_cards()
        for _ in range(global_vars.test_size):
            correct += frontend.question(next(cards))/5
        table.clear_user_cards()
        if correct / global_vars.test_size >= global_vars.min_win_rate:
            return 1
        return 0
