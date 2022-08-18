from django.db import models
from courses.models import Users


class UserInfo(models.Model):
    user_id = models.CharField('ID пользователя', max_length=50)
    user_email = models.CharField('E-mail', max_length=150)
    user_login = models.CharField('Логин', max_length=50)
    user_password = models.CharField('Пароль', max_length=40)
    name = models.CharField('Имя', max_length=40)
    last_name = models.CharField('Фамилия', max_length=40)
    age = models.IntegerField('Возраст')

    def __str__(self):
        return self.user_login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Account(models.Model):
    account_id = models.OneToOneField(Users, verbose_name='id', primary_key=True, on_delete=models.CASCADE)
    user_login = models.CharField('login', max_length=64)
    user_password = models.CharField('password', max_length=64)

    def __str__(self):
        return self.user_login

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        db_table = 'accounts'