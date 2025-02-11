from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('all/',alltodos.as_view(),name='alltodos'),
    path('add/',New_ToDo.as_view(),name = 'new_todo'),
    path('detail/<int:pk>/', Detail_ToDo.as_view(), name='todo_detail'),
    path('edit/<int:pk>/', TodoUpdateView.as_view(), name='edit_todo'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='delete_todo')

    
]