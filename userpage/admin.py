from django.contrib import admin
from .models import UserInfo
from .models import Account

admin.site.register(UserInfo)
admin.site.register(Account)
