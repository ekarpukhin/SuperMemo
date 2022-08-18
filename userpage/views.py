from django.shortcuts import render
from django.http import HttpResponse


def user_page_main(request):
    # data =
    return render(request, 'userpage/user_page.html')

