from django.urls import path
from .views import MainViewMain, AboutViewMain

urlpatterns = [
    path('', MainViewMain.as_view(), name='main_page'),
    path('about/', AboutViewMain.as_view(), name='about_info'),
]
