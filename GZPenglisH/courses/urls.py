from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses_main, name='courses_main'),
]
