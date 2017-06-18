# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from random import shuffle

VALUES = [
    'Item One',
    'Item Two',
    'Item Three',
    'Item Four',
    'Item Five',
    'Item Six',
    'Item Seven',
    'Item Eight',
    'Item Nine',
    'Item Ten',
    'Item Eleven',
    'Item Twelve',
    'Item Thirteen',
    'Item Fourteen',
    'Item Fifteen',
    'Item Sixteen',
    'Item Seventeen',
    'RANDOM WORDS!'
]


def index(request):
    context = {
        'num': 0,
        'msg': "Surprise Me!",
    }
    return render(request, 'surprise_me/index.html', context)


def results(request):
    shuffle(VALUES)
    num = int(request.POST['num'])
    lstSurprise = []
    if num > 17:
        num = 17
    elif num < 1:
        num = 1
    tmp = num

    for each in VALUES:
        lstSurprise += [each]
        tmp = tmp - 1
        if tmp == 0:
            break
    context = {
        'num': num,
        'list': lstSurprise,
        'msg': "Surprises:"
    }
    return render(request, 'surprise_me/index.html', context)