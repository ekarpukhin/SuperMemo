from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_page_main, name='user_page_main'),

    path('get_logininfo/', views.get_answer_form_js, name='getLoginInfo'),
]
