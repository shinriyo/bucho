# -*- encoding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import Inquery
from forms import InqueryForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

def add_new_inquery(request):
    user = User.objects.get(id=request.user.id)
    if request.POST:
        form = InqueryForm(request.POST)
        if form.is_valid():
            new_inquery = form.save()
            return HttpResponseRedirect('/inquery/updated/%s/' %(new_inquery.id))
    else:
        form = InqueryForm()
    return render_to_response('inquery/inquery_model_form.html',
        {'user':user,
        'id':id,
        'form':form})
#    return render_to_response('inquery/inquery_model_form.html', dict(form=form))

from django.http import HttpResponse

def inquery_updated(request, inquery_id):
    user = User.objects.filter(id=request.user.id)
    email = request.POST['email']
    description = request.POST['description']
    title = request.POST['type']
    result = send_mail(title , description, email, ['shinriyo@gmail.com'])
#   serult =  send_mail(title , description, email, [settings.DEFAULT_FROM_EMAIL])
    inquery = Inquery.objects.get(id=int(inquery_id))
    message = u'メッセージ送信が失敗しました。'

    if result > 0:
        message = u'メッセージ送信が完了いたしました。'
    
    return HttpResponse(message)
