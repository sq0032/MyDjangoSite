from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TodoList
import json

# Create your views here.
def todolist(request):
    
    if request.method == 'POST':
        name = request['POST'].name
        todolist = TodoList.objects.create(name = name)
    return JsonResponse()