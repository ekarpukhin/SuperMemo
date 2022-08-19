from django.contrib import admin
from .models import UserInfo
from .models import Account

"""Регистрируем модели в этом приложении для отображения на сайте в /admin"""

admin.site.register(UserInfo)
admin.site.register(Account)
