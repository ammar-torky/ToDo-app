from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')


def alltodos(request ):
    # variable for all items
    all_items = Todo.objects.all().order_by("-id")
    return render(request,'alltodos.html',{'all_items' : all_items})

def New_ToDo(request):
    if request.method == 'GET':
        form = AddNewTodo()
        return render(request, 'newtodos.html', {'form': form})
    elif request.method == 'POST':
        form = AddNewTodo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alltodos')
        