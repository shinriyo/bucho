# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from models import Csvdl
from django.contrib.auth.models import User
import datetime

class CsvForm(forms.ModelForm):
    class Meta:
        model = Csvdl

