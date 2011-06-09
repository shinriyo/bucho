# -*- encoding:utf-8 -*-
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name


PRIORITY_CHOICES=(('N', 'now'), ('S', 'soon'), ('L', 'later'))
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_finished = models.BooleanField(default=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='L')
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title[:10]+u'...'

