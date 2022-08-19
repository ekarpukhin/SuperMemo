from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .frontend import get_grade
from .SuperMemo import TeachingIter
from .DataBase import Table
from userpage.GlobalUser import get_user, get_login_status


class DataProcessing:
    """
    Связующий класс между алгоритмом и отображением карточек у пользователя
    В конструкторе находится пользователь и определяется текущий набор карточек для него
    Метод process() - оценивает ответ пользователя
    Метод next_word() - возвращает следующую карточку
    """
    def __init__(self):
        table = Table()
        table.user = get_user()
        print(get_user())
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
        if get_login_status("user"):
            card_iter = DataProcessing()
            try:
                question_word = card_iter.next_word().question
            except StopIteration:
                pass
        data = {
            "card": question_word,
            "end_day": False,

            "is_login": get_login_status("user"),
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
