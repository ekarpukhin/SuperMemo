class Card:
    def __init__(self, question, answer, I=1, n=0, EF=2.5):
        self.I = I
        self.n = n
        self.EF = EF
        self.question = question
        self.answer = answer

    def __str__(self):
        return str(self.__dict__)
