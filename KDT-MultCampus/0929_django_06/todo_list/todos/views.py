from django.shortcuts import render, redirect
from .models import Todo
import datetime


# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by("priority")
    
    now_time = datetime.date.today()
    context = {
        'todos':todos,
        'now_time':now_time,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')

    Todo.objects.create(content=content, priority=priority, deadline=deadline)
    return redirect('todos:index')

def change_status(request, todo_pk):
    todo = Todo.objects.get(id=todo_pk)
    if todo.completed == True:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def update_form(request, todo_pk):
    target = Todo.objects.get(id=todo_pk)
    todos = Todo.objects.all().order_by("priority")

    now_time = datetime.date.today()
    context = {
        'todos':todos,
        'target':target,
        'now_time':now_time,
    }
    return render(request, "todos/update-form.html", context)

def update(request, todo_pk):
    todo = Todo.objects.get(id=todo_pk)
    todo.priority = request.GET.get("priority")
    todo.content = request.GET.get("content")
    todo.deadline = request.GET.get("deadline")
    todo.save()

    return redirect("todos:index")

def delete(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    todo.delete()

    return redirect('todos:index')