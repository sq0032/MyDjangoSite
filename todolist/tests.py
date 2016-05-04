from django.test import TestCase
from todolist.models import TodoList, TodoItem
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client
client = Client()

# Create your tests here.

### Integration Test ###
class TodoListAPITests(TestCase):
    def test_if_created_todolist_successfully(self):
        client.post(reverse('create_todolist'), {'name':'test'})
        todolists = TodoList.objects.all()
        self.assertEqual(todolists.count(),1)
        self.assertEqual(todolists[0].name,'test')
        
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
