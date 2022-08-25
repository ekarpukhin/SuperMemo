from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .frontend import get_grade
from .SuperMemo import TeachingIter
from .DataBase import Table
from .models import Users


class DataProcessing:
    """
    Связующий класс между алгоритмом и отображением карточек у пользователя
    В конструкторе находится пользователь и определяется текущий набор карточек для него
    Метод process() - оценивает ответ пользователя
    Метод next_word() - возвращает следующую карточку
    """

    def __init__(self, username):
        table = Table()
        table.user = Users.objects.get(name=username)
        self.teach = TeachingIter(table=table)
        self.current_word = None

    def process(self, user_answer):
        grade = get_grade(self.current_word, user_answer)
        self.teach.process_card(grade)
        return grade

    def next_word(self):
        self.current_word = next(self.teach)
        return self.current_word


card_iter: DataProcessing


class CourseViewMain(View):
    """
    Класс отображения html-ки с карточками
    """

    def get(self, request, *args, **kwargs):
        global card_iter
        question_word = "That`s all for today!"
        if not request.user.is_authenticated:
            return redirect('main_page')
        card_iter = DataProcessing(request.user.username)
        try:
            question_word = card_iter.next_word().question
        except StopIteration:
            pass
        data = {
            "card": question_word,
            "end_day": False,

            "title": "Курсы",
        }
        return render(request, 'courses/courses_page.html', data)


@csrf_exempt
def get_answer_form_js(request):
    """
    Функция получающая ответ на карточку через ajax от пользователя
    Отправляет пользователю его оценку и следующее слово
    """
    user_answer = request.POST.get('user_answer')
    print(user_answer)
    answer_status = card_iter.process(user_answer)
    try:
        next_question_word = card_iter.next_word().question
        end_of_study = False
    except StopIteration:
        next_question_word = "That`s all for today!"
        end_of_study = True
    return JsonResponse(
        {'status': 'Todo added!', "responseText": user_answer, "answer_status": answer_status,
         "new_word": next_question_word, "end_of_study": end_of_study})


class LevelCheckViewMain(View):
    """
        Класс страницы определения уровня пользователя
    """

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('main_page')
        data = {
            "title": "Определение уровня",
            
            "level": 1
        }
        return render(request, 'courses/levelcheck_page.html', data)


@csrf_exempt
def get_lvlcheck_form_js(request):
    """
    Функция получающая ответ на карточку через ajax от пользователя при определении уровня
    Отправляет пользователю следующее слово
    """
    user_answer = request.POST.get('user_answer')
    print(user_answer)
    answer_status = 1
    try:
        next_question_word = "Faggot"
    except StopIteration:
        next_question_word = "The End!"
    return JsonResponse(
        {'status': 'Todo added!', "responseText": user_answer, "answer_status": answer_status,
         "new_word": next_question_word})
