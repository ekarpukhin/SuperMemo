from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_page_main, name='user_page_main'),
]
