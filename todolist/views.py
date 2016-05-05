from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404

from todolist.models import TodoList, TodoItem
import json

# Create your views here.
def todolist(request):
    if request.method == 'POST':
        name = request.POST['name']
        todolist = TodoList.objects.create(name = name)
        return JsonResponse({'name':name})
    elif request.method == 'GET':
        #TODO for Preet: Fetch and return lists data
        #lists data should be JSON format
        #[
        #    {'id':num, 'name':listname}
        #]
        return JsonResponse({'data':'goeshere'})
        
    raise Http404 


def todoitem(request, list_id):
#     print(list_id)
    if request.method == 'POST':
        name = request.POST['name']
        todolist = TodoList.objects.get(id=list_id)
        todoitem = TodoItem.objects.create(name=name, todolist=todolist)
    return JsonResponse({'name':'success'})