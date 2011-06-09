# -*- encoding:utf-8 -*-

from django.db import models

MEDAL_CHOICES = tuple([(i, i) for i in range(1, 11)])

class Answer(models.Model):
    comment = models.TextField(blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.comment[:10]+u'...'

class Question(models.Model):
    title = models.CharField(u'タイトル', max_length=200)
    descriotion = models.TextField('内容', blank=True)
    datetime_created = models.DateTimeField('日付', auto_now_add=True)
    is_finished = models.BooleanField('解決', default=False)
    medal = models.CharField('メダル', max_length=1, choices=MEDAL_CHOICES, default=1)
    answer = models.ForeignKey(Answer, verbose_name=u'回答')
#    answer = models.ForeignKey(Answer, blank=True, verbose_name=u'質問')

    def __unicode__(self):
        return self.title[:10]+u'...'
