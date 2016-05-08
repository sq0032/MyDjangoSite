'''
Created on May 3, 2016

@author: final_000
'''

from django.conf.urls import url

from todolist.views import todolist, todoitem, AAA

urlpatterns = [
    url(r'^$', todolist, name='todolist'),
    url(r'^(?P<list_id>\d+)/item$', todoitem, name='add_todoitem'),
    url(r'^AAA$', AAA, name='AAA'),
]
