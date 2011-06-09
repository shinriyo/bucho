# -*- encoding:utf-8 -*-
from models import Withdrawal
from django import forms

class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
