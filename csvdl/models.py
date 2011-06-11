# -*- encoding:utf-8 -*-

from django.db import models
from datetime import datetime
class Csvdl(models.Model):
    prev_date = models.DateTimeField(u'開始日時', default=datetime.now)
    end_date = models.DateTimeField(u'終了日時', default=datetime.now)

