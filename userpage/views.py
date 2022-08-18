from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Account
from .GlobalUser import set_user, set_account, get_account
from courses.models import Users


def user_page_main(request):
    # data =
    return render(request, 'userpage/user_page.html')


@csrf_exempt
def get_answer_form_js(request):
    value = {
        "login": request.POST.get('login'),
        "password":  request.POST.get('password')
    }
    try_account = Account.objects.get(user_login=value["login"])
    if try_account.user_password == value["password"]:
        print("I found this user")
        set_account(try_account)
        set_user(Users.objects.get(id=get_account().account_id.id))
        print("ejrhvoaeqrhfvouljaqehrglhavglhrlghlawehrguhqweu;rhghqer;lgh;lqehr;gh;qoerh;gohe;orhg;oehrg;qro;qg")
    print("Login: {}\tPassword: {}".format(value["login"], value["password"]))
    return JsonResponse(
        {'status': 'Success!', "responseText": value["login"]})
