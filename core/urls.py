from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('all/',alltodos,name='alltodos'),
    path('add/',New_ToDo,name = 'new_todo'),
]