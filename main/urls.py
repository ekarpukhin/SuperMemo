from django.urls import path
from .views import MainViewMain, AboutViewMain

"""
    Пути в приложении Main
"""

urlpatterns = [
    path('', MainViewMain.as_view(), name='main_page'),
    path('about/', AboutViewMain.as_view(), name='about_info'),
]
