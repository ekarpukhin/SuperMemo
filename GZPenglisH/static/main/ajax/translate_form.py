def get_answer_form_js(request):
    answer = request.POST.get('url')
    print("Your answer: {}".format(answer))
