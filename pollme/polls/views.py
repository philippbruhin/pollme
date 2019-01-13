from django.shortcuts import render

def polls_list(request):
    return render(request, 'polls/polls_list.html')
