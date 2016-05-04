from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from todolist.models import TodoList, TodoItem
import json

# Create your views here.
def todolist(request):
    if request.method == 'POST':
        name = request.POST['name']
        todolist = TodoList.objects.create(name = name)
    return JsonResponse({'name':name})


def todoitem(request, list_id):
    print(list_id)
    if request.method == 'POST':
        name = request.POST['name']
        todolist = TodoList.objects.get(id=list_id)
        todoitem = TodoItem.objects.create(name=name, todolist=todolist)
        
        
    return JsonResponse({'name':'good'})