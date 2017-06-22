# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import Users


# Create your views here.
def index(request):
    if 'showform' not in request.session:
        request.session['showform'] = True
    if 'showdata' not in request.session:
        request.session['showdata'] = False
    return render(request, "uname_validation/index.html")


def validate(request):
    nameLength = len(request.POST.get('name'))
    # validate name length
    if nameLength > 8 and nameLength < 26:
        # check if username exists
        if not Users.objects.filter(name=request.POST['name']).exists():
            Users.objects.create(name=request.POST['name'])
            request.session['last'] = request.POST['name']
            return redirect('/success')
        else:
            return redirect('/invalid')
    else:
        return redirect('/invalid')


def success(request):
    users = Users.objects.all()
    if users.count() > 0:
        context = {
            'users': users,
        }
        request.session['success'] = True
        request.session['showdata'] = True
        request.session['showform'] = False
        return render(request, "uname_validation/index.html", context)
    else:
        request.session['success'] = None
        request.session['showdata'] = False
        request.session['showform'] = True
        return redirect('/')


def invalid(request):
    request.session['success'] = False
    request.session['showdata'] = False
    request.session['showform'] = True
    return redirect('/')


def add(request):
    request.session['success'] = None
    request.session['showdata'] = False
    request.session['showform'] = True
    return redirect('/')


def remove(request, id):
    # delete user record
    Users.objects.get(id=id).delete()
    users = Users.objects.all()
    if users.count() == 0:
        request.session.clear()
        request.session['success'] = None
        request.session['showdata'] = False
        request.session['showform'] = True
        return redirect('/')

    return redirect('/success')
