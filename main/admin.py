from django.contrib import admin
from .models import MainInfo

"""Регистрируем модели в этом приложении для отображения на сайте в /admin"""

admin.site.register(MainInfo)
