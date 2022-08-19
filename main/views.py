from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from userpage.GlobalUser import get_login_status, get_username


class MainViewMain(View):
    """
    Класс отображения главной страницы
    """
    def get(self, request, *args, **kwargs):
        data = {
            "is_login": get_login_status("user"),
            "username": get_username()
        }
        return render(request, 'main/main_page.html', data)


class AboutViewMain(View):
    """
    Класс отображения страницы с информацией о проекте
    """
    def get(self, request, *args, **kwargs):
        data = {
            "is_login": get_login_status("user"),
            "username": get_username()
        }
        return render(request, 'main/about_info.html', data)
