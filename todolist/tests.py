from django.test import TestCase
from .models import TodoList

from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client
client = Client()

# Create your tests here.
# class TodoListMethodTests(TestCase):
#     def test_if_created_successfully(self):
        