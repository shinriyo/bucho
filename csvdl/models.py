from django.db import models

class Csvdl(models.Model):
    prev_date = forms.DateField(u'開始日時', initial=datetime.date.today)
    end_date = forms.DateField(u'終了日時', initial=datetime.date.today)

