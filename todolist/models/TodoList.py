from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=100)
    create_datetime = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name