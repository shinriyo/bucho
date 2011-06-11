# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from hello_view import *
from todo.views import *
from question.views import *
from withdrawal.views import *
from inquery.views import *
from bbs.views import *
from csvdl.views import *
from mysite.bbs.models import Thread
from django.conf import settings # for pic

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    url(r'^greet/$', hello),

    # TODO later delete
    url(r'^todo/categorized/$', show_categorized_list),
    url(r'^todo/search/$', search_todo),
    url(r'^todo/add/$', add_new_todo),
    url(r'^todo/edit/(?P<todo_id>\d+)/$', edit_todo),
    url(r'^todo/updated/(?P<todo_id>\d+)/$', todo_updated),
    # question page
    url(r'^question/show/$', show_question_list),
    url(r'^question/add/$', add_new_question),
    url(r'^question/updated/(?P<question_id>\d+)/$', question_updated),

    # withdrawal page
    url(r'^withdrawal/add/$', add_new_withdrawal),
    url(r'^withdrawal/updated/(?P<withdrawal_id>\d+)/$', withdrawal_updated),

    # inquery page
    url(r'^inquery/add/$', add_new_inquery),
    url(r'^inquery/updated/(?P<inquery_id>\d+)/$', inquery_updated),

    # for pics
    url(r'^static_site/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    #--------------
    #トップページ。スレッド一覧のページにリダイレクトする
#    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/1/'}),
    #スレッド一覧のページ
#    (r'^(?P<page>[0-9]+)/$',
    #url(r'^thread/(?P<page>\d+)/$', thread_list),
    url(r'^thread/list/$', thread_list),
#    url(r'^thread/$',
#        'django.views.generic.list_detail.object_list',
#        {'queryset': Thread.objects.all().order_by('-id'),
#        'paginate_by': 5,
#        'allow_empty': True}),

    #スレッドの新規作成ページ
    url(r'^thread/new/$', thread_new),
#    url(r'^thread/new/$',
#        'django.views.generic.create_update.create_object',
#        {'model': Thread,
#        'post_save_redirect': '/thread/'}),
    #スレッドの詳細ページ
    url(r'^thread/(?P<thread_id>\d+)/$', 'bbs.views.thread_detail'),

    # CSV download
    url(r'^csvdl/new/$', download_csv),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include('django.contrib.admin.urls')),

    (r'^accounts/', include('registration.urls')),
    (r'^$', direct_to_template, { 'template': 'index.html' }, 'index'),
    # mypage
    #TODO (r'^mypage/$', direct_to_template, { 'template': 'mypage.html' }, 'mypage'),
    (r'^mypage/$', 'register.views.mypage'),

    # added
    (r'^inquery_confirm$', direct_to_template, { 'template': 'registration/inquery_confirm.html' }, 'inquery'),
    (r'^question_confirm$', direct_to_template, { 'template': 'registration/question_confirm.html' }, 'question'),
)
