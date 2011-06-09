# -*- encoding:utf-8 -*-
from django.db import models

INQUERY_CHOICES=(('K', '広告掲載について'), ('B', 'buchoについて'), ('O', '教えて！goo関係者の者ですが'))
class Inquery(models.Model):
    email = models.CharField(u'メールアドレス', max_length=200)
    type = models.CharField(u'種別', max_length=1, choices=INQUERY_CHOICES, default='K')
    description = models.TextField(u'内容')
    datetime_created = models.DateTimeField(u'日付', auto_now_add=True)

    def __unicode__(self):
        return self.description[:10]+u'...'

