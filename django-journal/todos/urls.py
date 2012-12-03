from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'todos.views',
    url(r'^$', 'index'),
    url(r'^(?P<todo_id>\d+)/$', 'detail'),
    url(r'^(?P<todo_id>\d+)/change/$', 'change')
)
