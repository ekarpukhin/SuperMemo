class Card:
    def __init__(self, question, answer, I=1, n=0, EF=2.5):
        """
        :param question:
        :param answer:
        :param I: length of time (in days) SuperMemo will wait after the previous
         review before asking the user to review the card again
        :param n: number  of times the card has been successfully recalled
        (meaning it was given a grade ≥ 3) in a row since
        the last time it was not
        :param EF: The easiness factor EF, which loosely indicates how
         "easy" the card is (more precisely, it determines how
          quickly the inter-repetition interval grows).
        """
        self.I = I
        self.n = n
        self.EF = EF
        self.question = question
        self.answer = answer

    def __str__(self):
        return str(self.__dict__)
