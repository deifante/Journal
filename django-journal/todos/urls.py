from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'todos.views',
    url(r'^todos/$', 'index'),
    url(r'^todos/(?P<todo_id>\d+)/$', 'detail'),
)
