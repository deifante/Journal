from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

from todos.models import TodoList
from todos.forms import TodoListForm

def index(request):
    latest_todos_list = TodoList.objects.all().order_by('-created_date')[:5]
    return render_to_response('todos/index.html', {'latest_todos_list':latest_todos_list})

def detail(request, todo_id):
    todo_list = get_object_or_404(TodoList, pk=todo_id)
    form = TodoListForm(instance=todo_list)
    return render_to_response('todos/detail.html', {'todo':todo_list, 'form':form},
                              context_instance=RequestContext(request))

def change(request, todo_id):
    t = get_object_or_404(TodoList, pk=todo_id)
    if request.method == 'POST': # If the form has been submitted
        form = TodoListForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            print 'form is valid'
            # Process the data in form.cleaned_data
            print form
            return HttpResponseRedirect(reverse('todos.views.thanks'))
        else:
            print 'form not valid'
    else:
        form = TodoListForm()
    response_dict = {'todo':t, 'form': form}
    return render_to_response(
        'todos/change.html',
        response_dict,
        context_instance=RequestContext(request))

    # try:
    #     selected_items = 1
    # except (KeyError, LineItem.DoesNotExist):
    #     return render_to_response('todos/detail.html',
    #                               {'todo':t,
    #                                'error_message':'Invalid choice selection.'},
    #                               context_instance=RequestContext(request))
    # else:
    #     selected_items = 2
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('todos.views.index'))
                                  
