from django.urls import path
from .views import UserPageViewMain, get_login_form_js

"""
    Пути в приложении Userpage
    'get_logininfo/' - функция в python получающая и обрабатывающая информацию о попытке входа в аккаунт
"""

urlpatterns = [
    path('', UserPageViewMain.as_view(), name='user_page_main'),

    path('get_logininfo/', get_login_form_js, name='getLoginInfo'),
]
