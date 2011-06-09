# -*- coding: utf-8 -*-
from django.forms import ModelForm
from mysite.bbs.models import Thread, Comment

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        exclude = ('target_user', 'is_finished', )

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ('target_user', 'thread', )
