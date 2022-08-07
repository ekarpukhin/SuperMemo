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
                print('jopa')
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
        win_rate = 0
        i = 0
        table = Table(self)
        table.load_random_cards()
        cards = table.get_cards()
        while i < global_vars.test_size:
            if frontend.question(next(cards)):
                win_rate += 1
            i += 1
        table.clear_user_cards()
        if win_rate >= global_vars.min_win_rate:
            return 1
        return 0
