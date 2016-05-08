from django.db import models
from TodoList import TodoList

# Create your models here.    
class TodoItem(models.Model):
    name = models.CharField(max_length=100)
    todolist = models.ForeignKey(TodoList)
    create_datetime = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name