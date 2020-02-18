from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import *


def index(req):
    todos = Todo.objects.all()
    content = {'todos': todos}

    return render(req, 'todolist/index.html', content)


def createTodo(req):
    user_input_str = req.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))


def doneTodo(req):
    done_todo_id = req.GET['todoNum']
    print("완료한 todo의 id", done_todo_id)
    todo = Todo.objects.get(id=done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))

# Create your views here.
