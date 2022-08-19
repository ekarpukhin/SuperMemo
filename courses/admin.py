from django.contrib import admin
from .models import Courses

"""Регистрируем модели в этом приложении для отображения на сайте в /admin"""

admin.site.register(Courses)
