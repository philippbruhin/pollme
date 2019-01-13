from django.http import HttpResponse
from django.shortcuts import render

def polls_list(request):
    return HttpResponse('polls list')
