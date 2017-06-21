# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import datetime
# the index function is called when root is visited


def index(request):
    now = datetime.datetime.now()
    context = {
        "datetime": now.strftime("%Y-%m-%d %H:%M"),
    }
    return render(request, 'time_display_assignment/index.html', context)
