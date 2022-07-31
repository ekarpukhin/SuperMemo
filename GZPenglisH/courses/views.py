from django.shortcuts import render
from django.http import HttpResponse
# from static.main_algorithm import User


def courses_main(request):
    # user = User.User('Kostya')
    card = 'ЖОПА'
    data = {
        'card': card,
    }
    return render(request, 'courses/courses_page.html', data)


def get_answer_from_js(request):
    answer = request.POST.get('url')
    print("Your answer: {}".format(answer))

