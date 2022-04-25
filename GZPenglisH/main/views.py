from django.shortcuts import render
from django.http import HttpResponse


def main_main(request):
    # data =
    return render(request, 'main/main_page.html')


def about_info(request):
    # data =
    return render(request, 'main/about_info.html')
