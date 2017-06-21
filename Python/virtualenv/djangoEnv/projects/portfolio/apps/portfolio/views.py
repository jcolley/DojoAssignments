# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse


def index(request):
    print "*" * 50
    return render(request, 'portfolio/index.html')


def testimonials(request):
    print "*" * 50
    return render(request, 'portfolio/testimonials.html')