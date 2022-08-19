from django.urls import path
from . import views

"""
    Пути в приложении Userpage
    'get_logininfo/' - функция в python получающая и обрабатывающая информацию о попытке входа в аккаунт
    'get_logout/' - функция в python обрабатывающая выход из аккаунта
    'get_signup/' - функция в python получающая и обрабатывающая информацию о регистрации аккаунта
"""

urlpatterns = [
    path('', views.UserPageViewMain.as_view(), name='user_page_main'),

    path('get_logininfo/', views.get_login_form_js, name='getLoginInfo'),
    path('get_logout/', views.get_logout_form_js, name='getLogout'),
    path('get_signup/', views.get_signup_form_js, name='getSignUp'),
]
