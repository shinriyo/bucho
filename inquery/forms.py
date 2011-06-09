# -*- encoding:utf-8 -*-
from models import Inquery
from django import forms

class InqueryForm(forms.ModelForm):
    class Meta:
        model = Inquery

    def clean_email(self):
        email = self.cleaned_data['email']
        if(email.find('@')):
            raise forms.ValidationError(u'メールアドレスは@が必須です。')
        return email
