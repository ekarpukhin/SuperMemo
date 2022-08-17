from django.db import models




class Courses(models.Model):
    title = models.CharField('Название курса', max_length=100)
    anons = models.CharField('О курсе', max_length=250)
    text_all = models.TextField('Описание')
    date = models.DateTimeField('Время создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


