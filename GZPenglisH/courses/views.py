from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from static.engine.SuperMemo import TeachingIter
from static.engine.DataBase import Table
from static.engine.frontend import grade as get_grade


class DataProcessing:
    def __init__(self, username):
        table = Table()
        user = table.get_user(username)
        self.teach = TeachingIter(user)
        self.current_word = None

    def process(self, user_answer):
        grade = get_grade(self.current_word, user_answer)
        self.teach.process_card(grade)
        return grade

    def next_word(self):
        self.current_word = next(self.teach)
        return self.current_word


username = "Ivan"
card = DataProcessing(username)


class CourseViewMain(View):

    def get(self, request, *args, **kwargs):
        data = {
            "card": card.next_word().question,
            # "card": "Plat",
        }
        return render(request, 'courses/courses_page.html', data)


@csrf_exempt
def get_answer_form_js(request):
    answer = request.POST.get('url')
    print(answer)
    answer_status = card.process(answer)
    return JsonResponse(
        {'status': 'Todo added!', "responseText": answer, "answer_status": answer_status,
         "new_word": card.next_word().question})
         # "new_word": "Aboba"})
# Сделать нормально
