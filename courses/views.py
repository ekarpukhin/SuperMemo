from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .frontend import grade as get_grade
from .SuperMemo import TeachingIter
from .DataBase import Table
from userpage.GlobalUser import get_user

card = None

class DataProcessing:
    def __init__(self, username):
        table = Table()
        self.teach = TeachingIter(table.get_user(username))
        self.current_word = None
        self.end_day = False

    def process(self, user_answer):
        grade = get_grade(self.current_word, user_answer)
        self.teach.process_card(grade)
        return grade

    def next_word(self):
        self.current_word = next(self.teach)
        return self.current_word


class CourseViewMain(View):
    def get(self, request, *args, **kwargs):
        global card
        card = DataProcessing(get_user().name)
        try:
            question_word = card.next_word().question
        except StopIteration:
            question_word = "That`s all for today!"
        data = {
            "card": question_word,
            "end_day": card.end_day,

            "is_login": False,
        }
        return render(request, 'courses/courses_page.html', data)


@csrf_exempt
def get_answer_form_js(request):
    user_answer = request.POST.get('user_answer')
    print(user_answer)
    answer_status = card.process(user_answer)
    try:
        next_question_word = card.next_word().question
        end_of_study = False
    except StopIteration:
        next_question_word = "That`s all for today!"
        end_of_study = True
        card.end_day = True
    return JsonResponse(
        {'status': 'Todo added!', "responseText": user_answer, "answer_status": answer_status,
         "new_word": next_question_word, "end_of_study": end_of_study})
