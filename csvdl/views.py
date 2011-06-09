# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from forms import CsvForm

def download_csv(request):
    form, results = None, []
    if request.GET:
        form = CsvForm(request.POST)
        if form.is_valid():
            cleaned = form.clean()
            queryset = User.objects.all()
            prev_date = cleaned['prev_date']
            if prev_date:
                queryset = queryset.filter(date_joined__gte=prev_date) # >=
            include_jinished = cleaned.get('include_finished', False)
            # P75見て復習
            if finished_date:
                queryset = queryset.filter(date_joined__lte=finished_date) # <=
            results = queryset
    else:
        form = CsvForm()
    return render_to_response('search_form.html', dict(form=form, results=results))
