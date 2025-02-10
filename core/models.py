from django.db import models

# Create your models here.
class Todo(models.Model):
     text = models.TextField(max_length=500)

     # this is used to return the text of the todo item
     def __str__(self):
          return self.text
     



