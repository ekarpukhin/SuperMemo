from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class CourseViewMain(View):

    def get(self, request, *args, **kwargs):
        card = "Platypus"
        data = {
            "card": card,
        }
        return render(request, 'courses/courses_page.html', data)


def get_answer_form_js(request):
    answer = request.POST.get('url')
    print("Your answer: {}".format(answer))
