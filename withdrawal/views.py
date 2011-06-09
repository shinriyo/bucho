# -*- encoding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import Withdrawal
#from django import forms
from forms import WithdrawalForm
from django.contrib.auth.models import User

def add_new_withdrawal(request):
    user = User.objects.filter(id=request.user.id)
    if request.POST:
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            new_withdrawal = form.save()
            return HttpResponseRedirect('/withdrawal/updated/%s/' %(new_withdrawal.id))
    else:
        form = WithdrawalForm()
    return render_to_response('withdrawal/withdrawal_model_form.html', dict(form=form))

from django.http import HttpResponse

def withdrawal_updated(request, withdrawal_id):
    user = User.objects.filter(id=request.user.id)
    withdrawal = Withdrawal.objects.get(id=int(withdrawal_id))
    message = u'退会手続きを完了いたしました。'
    return HttpResponse(message)
