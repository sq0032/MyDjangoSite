from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=100)
    create_datetime = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
    
    
class TodoItem(models.Model):
    name = models.CharField(max_length=100)
    todolist = models.ForeignKey(TodoList)
    create_datetime = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name    