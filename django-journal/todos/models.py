import datetime
from django.utils import timezone
from django.db import models

class TodoList(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('Date created', auto_now_add=True)

    def __unicode__(self):
        return self.description

class LineItem(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('Date created', auto_now_add=True)
    my_list = models.ForeignKey(TodoList)
    is_done = models.BooleanField()

    def was_created_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)

    def __unicode__(self):
        return self.description
