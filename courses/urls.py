from django.urls import path
from .views import CourseViewMain
from . import views

"""
    Пути в приложении Courses
'get_answer/' - функция в python получения введенного ответа на карточку
"""

urlpatterns = [
    path('', CourseViewMain.as_view(), name='courses_main'),
    path('get_answer/', views.get_answer_form_js, name='getAnswer'),
]
