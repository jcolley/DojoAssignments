# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Authors, Categories


# Create your views here.
def index(response):
    books = Books.objects.all()
    context = {
        'books': books,
    }
    return render(response, "books_fs/index.html", context)


def addbook(request):
    author = Authors.objects.create(name=request.POST['author'])
    category = Categories.objects.create(category=request.POST['category'])
    Books.objects.create(title=request.POST['title'], author=author, category=category)
    return redirect('/')
