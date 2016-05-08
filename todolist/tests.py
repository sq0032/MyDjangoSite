from django.test import TestCase
from todolist.models import TodoList, TodoItem
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client
client = Client()

import json
# Create your tests here.

def add(x, y):
    return x+y


class SampleTests(TestCase):
    def test_if_1_equal_1(self):
        self.assertEqual(1, 1)
        
    def test_if_add_works(self):
        self.assertEqual(add(3,5), 8)

#class AAATests(TestCase):
#    def test_AAA(self):
#        r = client.put(reverse("AAA"),json.dumps({"name":"test"}))
#        self.assertEqual(r.content, 'O')

## Integration Test ###
class TodoListAPITests(TestCase):
    def test_if_created_todolist_successfully(self):
        client.post(reverse('todolist'), {'name':'test'})
        todolists = TodoList.objects.all()
        self.assertEqual(todolists.count(),1)
        self.assertEqual(todolists[0].name,'test')
        
#     def test_if_fetch_todolist_successfully(self):
#         #initial json
#         d = [
#              {'id':1, 'name':'test1'},
#              {'id':2, 'name':'test2'},
#              {'id':3, 'name':'test3'},
#         ]
#         
#         #Insert initial todolists
#         TodoList.objects.create(id=1, name="test1")
#         TodoList.objects.create(id=2, name="test2")
#         TodoList.objects.create(id=3, name="test3")
#         
#         response = client.get(reverse('todolist'))
#         self.assertEqual(response.content, json.dumps(d))
         
class TodoItemAPITests(TestCase):
    def test_if_created_todoitem_successfully(self):
        todolist = TodoList.objects.create(name='test list')
        client.post(reverse('add_todoitem', kwargs={'list_id':todolist.id}), {'name':'test item'})
        todoitems = TodoItem.objects.all()
        self.assertEqual(todoitems.count(),1)
        self.assertEqual(todoitems[0].name,'test item')
        

 


### Unit Test ###
class TodoListMethodTests(TestCase):
    def test_if_created_todolist_successfully(self):
        TodoList.objects.create(name="test")
        todolists = TodoList.objects.all()
        self.assertEqual(todolists.count(),1)
        self.assertEqual(todolists[0].name,'test')
        
         
class TodoItemMethodTests(TestCase):
    def test_if_created_todoitem_successfully(self):
        todolist = TodoList.objects.create(name="test list")
        TodoItem.objects.create(name="test item", todolist=todolist)
        todoitems = TodoItem.objects.all()
        self.assertEqual(todoitems.count(),1)
        self.assertEqual(todoitems[0].name,'test item')        
