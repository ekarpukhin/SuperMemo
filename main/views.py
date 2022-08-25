from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class MainViewMain(View):
    """
    Класс отображения главной страницы
    """
    def get(self, request, *args, **kwargs):
        data = {
            "title": "Главная"
        }
        return render(request, 'main/main_page.html', data)


class AboutViewMain(View):
    """
    Класс отображения страницы с информацией о проекте
    """
    def get(self, request, *args, **kwargs):
        data = {
            "title": "О нас"
        }
        return render(request, 'main/about_info.html', data)
