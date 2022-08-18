from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .frontend import grade as get_grade
from .SuperMemo import TeachingIter
from .DataBase import Table


class DataProcessing:
    def __init__(self, username):
        table = Table()
        user = table.get_user(username)
        self.teach = TeachingIter(user)
        self.current_word = None
        self.end_day = False

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
        try:
            question_word = card.next_word().question
        except  StopIteration:
            question_word = "That`s all for today!"
        data = {
            "card": question_word,
            "end_day": card.end_day,
        }
        return render(request, 'courses/courses_page.html', data)


@csrf_exempt
def get_answer_form_js(request):
    user_answer = request.POST.get('url')
    print(user_answer)
    answer_status = card.process(user_answer)
    try:
        next_question_word = card.next_word().question
        end_of_study = False
    except  StopIteration:
        next_question_word = "That`s all for today!"
        end_of_study = True
        card.end_day = False
    return JsonResponse(
        {'status': 'Todo added!', "responseText": user_answer, "answer_status": answer_status,
         "new_word": next_question_word, "end_of_study": end_of_study})
# Сделать нормально
