from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class MainViewMain(View):

    def get(self, request, *args, **kwargs):
        # data =
        return render(request, 'main/main_page.html')


class AboutViewMain(View):

    def get(self, request, *args, **kwargs):
        # data =
        return render(request, 'main/about_info.html')
