from django.template import Context, loader
from todos.models import TodoList
from django.http import HttpResponse

def index(request):
    
