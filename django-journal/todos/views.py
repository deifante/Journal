from django.template import Context, loader
from todos.models import TodoList
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    latest_todos_list = TodoList.objects.all().order_by('-created_date')[:5]
    return render_to_response('todos/index.html', {'latest_todos_list':latest_todos_list})

def detail(request, todo_id):
    t = get_object_or_404(TodoList, pk=todo_id)
    return render_to_response('todos/detail.html', {'todo':t})
