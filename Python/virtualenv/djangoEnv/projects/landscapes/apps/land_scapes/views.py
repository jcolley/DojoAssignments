# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def index(request):
    context = {
        'msg': 'Welcome! Enter any number 1-50 as a url parameter, for example "/32"',
        'img': '1'
    }

    return render(request, 'land_scapes/index.html', context)


def landscape(request, num):
    num = int(num)
    if num > 0 and num <= 50:
        if num >= 1 and num <= 10:
            img = 'snow.jpg'
        elif num >= 11 and num <= 20:
            img = 'desert.jpg'
        elif num >= 21 and num <= 30:
            img = 'forrest.jpg'
        elif num >= 31 and num <= 40:
            img = 'vinyard.jpg'
        else:
            img = 'tropical.jpg'

        context = {
            'msg': '',
            'img': img,
        }
    else:
        context = {
            'msg': "Chosen number is out of range (0-50)",
            'img': '1',
        }
    return render(request, 'land_scapes/index.html', context)
