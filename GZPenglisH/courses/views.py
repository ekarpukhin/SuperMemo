from django.shortcuts import render
from django.http import HttpResponse


def courses_main(request):
    card = "Platypus"
    data = {
        "card": card,
    }
    return render(request, 'courses/courses_page.html', data)

