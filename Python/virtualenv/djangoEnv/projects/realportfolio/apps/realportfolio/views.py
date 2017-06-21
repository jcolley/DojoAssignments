# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
# the index function is called when root is visited


def index(request):
    print "*" * 50
    return render(request, 'realportfolio/index.html')


def about(request):
    print "*" * 50
    return render(request, 'realportfolio/about.html')


def testimonials(request):
    print "*" * 50
    return render(request, 'realportfolio/testimonials.html')


def projects(request):
    print "*" * 50
    return render(request, 'realportfolio/projects.html')
