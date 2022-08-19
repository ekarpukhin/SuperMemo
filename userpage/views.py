from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from .models import Account
from .GlobalUser import set_user, set_account, get_account, get_login_status, get_username
from courses.models import Users


class UserPageViewMain(View):
    """
        Класс отображения html-ки-страницы пользователя
    """
    def get(self, request, *args, **kwargs):
        data = {
            "is_login": get_login_status("user"),
            "username": get_username()
        }
        return render(request, 'userpage/user_page.html', data)


@csrf_exempt
def get_login_form_js(request):
    """
        Функция, получающая логин и пароль при попытке входа
        Ищет в БД пользователя по логину и
        присваевает глобальным переменным пользователя соответствующие значения
    """
    value = {
        "login": request.POST.get('login'),
        "password":  request.POST.get('password')
    }
    print("Login: {}\tPassword: {}".format(value["login"], value["password"]))
    try:
        try_account = Account.objects.get(user_login=value["login"])
    except ObjectDoesNotExist:
        return JsonResponse({'status': 'Fail', "responseText": "login incorrect"})
    if try_account.user_password == value["password"]:
        print("I found this user")
        set_account(try_account)
        set_user(Users.objects.get(id=get_account().account_id.id))
        return JsonResponse({'status': 'Success', "responseText": value["login"]})
    else:
        return JsonResponse({'status': 'Fail', "responseText": "password incorrect"})
