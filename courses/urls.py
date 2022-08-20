from django.urls import path
from . import views

"""
    Пути в приложении Courses
'get_answer/' - функция в python получения введенного ответа на карточку
"""

urlpatterns = [
    path('', views.CourseViewMain.as_view(), name='courses_main'),
    path('level_check/', views.LevelCheckViewMain.as_view(), name='levelcheck_main'),
    path('get_answer/', views.get_answer_form_js, name='getAnswer'),
    path('get_levelcheck/', views.get_lvlcheck_form_js, name='getLVLcheck'),
]
