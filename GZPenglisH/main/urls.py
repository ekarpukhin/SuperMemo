from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_main, name='main_page'),
    path('about/', views.about_info, name='about_info'),
]
