# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import datetime
MEDAL_CHOICES = tuple([(str(i), int(i)) for i in range(1, 11)])

from django.db import models
from django.contrib.auth.models import User
class ExtendUser(models.Model):
    medal = models.IntegerField(blank=True)
    user = models.ForeignKey(User, unique=True)

class Thread(models.Model):
    target_user = models.ForeignKey(User, unique=False, verbose_name=u'ユーザ', blank=False)
#    target_user = models.ForeignKey(User, unique=True, verbose_name=u'ユーザ', blank=False)
    title = models.CharField(u'タイトル', max_length=200, blank=False)
    message = models.TextField(u'内容', blank=False)
    medal = models.CharField('メダル', max_length=2, choices=MEDAL_CHOICES, default='1')
    is_finished = models.BooleanField('解決', default=False)
    pub_date = models.DateTimeField(u'登録日時', auto_now_add=True, editable=False)

    class Meta:
        verbose_name = u'スレッド'

    def __unicode__(self):
        return self.message

class Comment(models.Model):
    target_user = models.ForeignKey(User, unique=False)
    thread = models.ForeignKey(Thread, verbose_name=u'スレッド')
    message = models.CharField('', max_length=200, blank=False)
    pub_date = models.DateTimeField(u'登録日時', auto_now_add=True, editable=False)

    class Meta:
        verbose_name = u'コメント'
    def __unicode__(self):
        return self.message

    def time_from_pub_date(self):
        timedelta = datetime.datetime.now() - self.pub_date
        delta = timedelta.seconds
        if delta > 60:
            delta = delta/60
            if delta > 24:
                delta = str(delta/24)+'日'
            else:
                delta = str(delta)+'時間'
        else:
            delta = str(delta)+'分'
        return delta
