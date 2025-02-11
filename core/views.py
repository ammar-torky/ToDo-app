from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



# Create your views here.
def index(request):
    return render(request,'index.html')


class alltodos(ListView):
    model = Todo
    template_name = 'alltodos.html'
    paginate_by = 10
    def get_queryset(self):
        return Todo.objects.all().order_by('-id')


class New_ToDo(CreateView):
    model = Todo
    fields = ['text']
    template_name = 'newtodos.html'
    #the forward link after complete
    success_url = '/all/'

class Detail_ToDo(DetailView):
    model = Todo
    template_name = 'todo_detail.html'

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['text']
    template_name = 'updateToDo.html'
    #the forward link after complete
    success_url = '/all/'

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'deleteToDo.html'
    success_url = '/all/'