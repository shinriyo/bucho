# -*- coding: utf-8 -*-

from django.http import HttpResponse

def hello(request):
    """Simply displays greeting message.
    """
    message = "<html><body>Hello, Django!</body></html>"
    return HttpResponse(message)

from django.http import HttpResponse, Http404

def hello_error(request):
    """Simply raise Http404
    """
    raise Http404
