# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    context = {
        "color": "none",
    }
    return render(request, 'dNinjas/index.html', context)


def ninja(request):
    context = {
        "color": False,
    }
    return render(request, 'dNinjas/index.html', context)


def ninjas(request, color):
    context = {
        "color": color,
        "img1": "dNinjas/img/leonardo.jpg",
        "img2": "dNinjas/img/michelangelo.jpg",
        "img3": "dNinjas/img/raphael.jpg",
        "img4": "dNinjas/img/donatello.jpg",
        "img5": "dNinjas/img/notapril.jpg",
    }
    return render(request, 'dNinjas/index.html', context)
