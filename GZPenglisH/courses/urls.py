from django.urls import path
from .views import CourseViewMain

urlpatterns = [
    path('', CourseViewMain.as_view(), name='courses_main'),
]
