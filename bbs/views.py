# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from mysite.bbs.models import Thread, Comment, ExtendUser
from mysite.bbs.forms import ThreadForm, CommentForm
import datetime
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import User

def thread_new(request):
    user = User.objects.filter(id=request.user.id)
    if request.POST:
        form = ThreadForm(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            exuser = ExtendUser.objects.get(target_user=request.user.id) # answered
            exuser.medal -= request.POST['medal']
            u.target_user = request.user
            u.save()
            return HttpResponseRedirect('/thread/list/')
    else:
        form = ThreadForm()
    commented_list = Comment.objects.filter(target_user=request.user.id) # answered
    thread_list = Thread.objects.all()

    return render_to_response('bbs/thread_form.html',
        {'commented_list': commented_list,
         'user': user,
         'thread_list': thread_list,
         'form': form})

def thread_list(request):
    user = User.objects.filter(id=request.user.id)
    commented_list = Comment.objects.filter(target_user=request.user.id) # answered
    thread_list = Thread.objects.all()

    paginator = Paginator(thread_list, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(pagenator.num_page)

    return render_to_response('bbs/thread_list.html',
        {'commented_list': commented_list,
         'thread_list': thread_list,
         'contacts': contacts})

def thread_detail(request, thread_id):
    '''
    指定したスレッドを表示する。
    @param thread_id: スレッドID
    '''

    thread = get_object_or_404(Thread, pk=thread_id)
    # コメントをかいたことがある
    wrote = thread.comment_set.filter(id=request.user.id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.thread = thread
            comment.target_user_id = request.user.id
            # 書いた経験がなければ書ける
            if not wrote:
                comment.save()
            form = CommentForm() # initialize form
    else:
        form = CommentForm()
    comment_list = thread.comment_set.all().order_by('id')

    thread_list = Thread.objects.filter(target_user=request.user.id)
    commented_list = Comment.objects.filter(target_user=request.user.id) # answered

    return render_to_response('bbs/thread_detail.html',
    {'thread': thread,
        'user': user,
        'thread_list': thread_list, #最近した質問
        'commented_list': commented_list, #最近した回答
        'comment_list': comment_list,
        'wrote': wrote,
        'form': form})

