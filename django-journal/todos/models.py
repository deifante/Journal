from django.db import models

class List(models.Model):
    description = models.CharField(max_length=200)

class LineItem(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('Date this item was created')
    my_list = models.ForeignKey(List)
    is_done = models.BooleanField()
