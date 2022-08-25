from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .utils import *
from .forms import *
from courses.models import Users


class RegisterUser(DataMixin, CreateView):
    """
        Класс регистрации нового пользователя (отдельная страничка)
        После регистрации, пользователь автоматически входит в аккаунт
    """
    form_class = RegisterUserForm
    template_name = 'userpage/register.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        print("Login: ", self.request.POST['username'], "Password: ", self.request.POST['password1'])
        user = authenticate(username=self.request.POST['username'], password=self.request.POST['password1'])
        login(self.request, user)
        return reverse_lazy('create_user')


def create_user_in_table(request):
    """Сразу после регистрации в табличке users создается соответствующая строка"""
    if request.user.is_authenticated:
        user = Users(name=request.user.username, level=1)
        user.save()
    return redirect('main_page')


def logout_user(request):
    """Выход из аккаунта"""
    logout(request)
    return redirect('main_page')


class LoginUser(DataMixin, LoginView):
    """
            Класс входа пользователя (отдельная страничка)
    """
    form_class = LoginUserForm
    template_name = 'userpage/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main_page')


class UserPageViewMain(View):
    """
        Класс отображения html-ки-страницы пользователя
    """
    def get(self, request, *args, **kwargs):
        _user = Users.objects.get(name=request.user.username)
        if not request.user.is_authenticated:
            return redirect('main_page')
        data = {
            "my_user": _user,

            "title": "Личный кабинет",
        }
        return render(request, 'userpage/user_page.html', data)
