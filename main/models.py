from django.db import models


class MainInfo(models.Model):
    """
    Не используемый класс для отображения какой-то информации/новостей на главной странице
    """
    title = models.CharField('Название', max_length=100)
    text_all = models.TextField('Текст')
    date = models.DateTimeField('Время создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
