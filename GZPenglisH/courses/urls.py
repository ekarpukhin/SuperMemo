from django.urls import path
from .views import CourseViewMain
from . import views

urlpatterns = [
    path('', CourseViewMain.as_view(), name='courses_main'),
    path('get_answer/', views.get_answer_form_js, name='courses_main')
]
