# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
# the index function is called when root is visited


def index(request):
    print "hello world"
    return render(request, 'HelloWorld/index.html')
