from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt



class CourseViewMain(View):

    def get(self, request, *args, **kwargs):
        card = "Platypus"
        data = {
            "card": card,
        }
        return render(request, 'courses/courses_page.html', data)

@csrf_exempt
def get_answer_form_js(request):
    answer = request.POST.get('url')
    if answer == "aboba":
        answer_status = True
    else:
        answer_status = False
    return JsonResponse({'status': 'Todo added!', "responseText": answer, "answer_status": answer_status})
