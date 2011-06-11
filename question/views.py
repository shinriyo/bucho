# -*- encoding:utf-8 -*-
from django.shortcuts import render_to_response
from models import Question
#from django import forms

def show_question_list(request):
    return render_to_response('question_list.html',
            dict(questions=Question.objects.all()))

from django.http import HttpResponseRedirect
from forms import QuestionForm

def add_new_question(request):
    if request.POST:
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save()
#            return HttpResponseRedirect('/question/updated/%s/' %(new_question.id))
            return HttpResponseRedirect('/question/show/')
    else:
        form = QuestionForm()
    return render_to_response('question_model_form.html', dict(form=form))

"""
def edit_todo(request, todo_id):
    todo_instance = get_object_or_404(Todo, pk=todo_id)
    if request.POST:
        form = TodoForm(request.POST, instance=todo_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo/updated/%s/' %(todo_id))
        else:
            form = TodoForm(instance=todo_instance)
        return render_to_response('model_form.html', dict(form=form))
"""

from django.http import HttpResponse

def question_updated(request, question_id):
    question = Question.objects.get(id=int(question_id))
    message = u'AAAAAAA' %(question.title)
    return HttpResponse(message)

