# -*- encoding:utf-8 -*-
from django.db import models

class Withdrawal(models.Model):
# uer number id??
    reason = models.TextField(u'退会理由')
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title[:10]+u'...'
