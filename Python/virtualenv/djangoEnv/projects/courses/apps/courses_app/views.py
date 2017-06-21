# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Courses


# All them views, yo:
def index(response):
    courses = Courses.objects.all()
    context = {
        'courses': courses,
    }
    return render(response, "courses_app/index.html", context)


def addCourse(request):
    course = Courses.objects.create(
        name=request.POST['name'],
        description=request.POST['description']
    )

    return redirect('/')


def youSure(request, id):
    course = Courses.objects.get(id=id)

    context = {
        'course': course,
    }
    return render(request, "courses_app/youSure.html", context)


def destroy(request):
    Courses.objects.get(id=request.POST['id']).delete()
    return redirect('/')
