# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from mysite.bbs.models import ExtendUser, Thread, Comment
from django.contrib.auth.models import User

def mypage(request):
    user = User.objects.get(id=request.user.id)
    exuser = ExtendUser.objects.get(user=request.user.id) # answered

    #thread = Thread.objects.get(target_user_id=request.user.id) # answered
    thread_list = Thread.objects.filter(target_user=request.user.id) # answered
    #comment = Comment.objects.get(target_user_id=request.user.id) # answered
    commented_list = Comment.objects.filter(target_user=request.user.id) # answered


    return render_to_response('mypage.html',
        {'user': user,
         'thread_list': thread_list,
         'commented_list': commented_list,
         'exuser': exuser})

