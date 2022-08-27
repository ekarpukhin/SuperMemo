from django.db import models


class Cards(models.Model):
    """
        Класс карточки слова
    """
    id = models.IntegerField('id', primary_key=True, )
    level = models.IntegerField('level')
    content = models.TextField('content')

    class Meta:
        db_table = "cards"


class Users(models.Model):
    """
        Класс пользователя, для нахождения его в БД основного алгоритма
    """
    id = models.IntegerField('id', primary_key=True)
    name = models.CharField('name', max_length=255)
    level = models.IntegerField('level')

    class Meta:
        db_table = "users"


class CardsInfo(models.Model):
    """
        Связующий класс в таблице для пользователя и карточки
    """
    id = models.IntegerField('id', primary_key=True)
    user_id = models.ForeignKey(Users, verbose_name='user', on_delete=models.CASCADE)
    card_id = models.ForeignKey(Cards, verbose_name='card', on_delete=models.CASCADE)
    card_info = models.TextField('info')

    class Meta:
        db_table = "cards_info"


class Courses(models.Model):
    """
        Пока абсолютно бесполезный класс, который скорее всего придется удалить. В последующем для разных курсов
    """
    title = models.CharField('Название курса', max_length=100)
    anons = models.CharField('О курсе', max_length=250)
    text_all = models.TextField('Описание')
    date = models.DateTimeField('Время создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class RussianWords(models.Model):
    word = models.CharField('word', max_length=255)
    cut = models.CharField('cut', max_length=255)

    class Meta:
        db_table = 'russian_words'