# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse


def index(request):
    render(request, 'products_app/index.html')
