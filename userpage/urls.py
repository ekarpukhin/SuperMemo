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
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('create_user/', views.create_user_in_table, name='create_user'),
    path('logout/', views.logout_user, name='logout'),
]
