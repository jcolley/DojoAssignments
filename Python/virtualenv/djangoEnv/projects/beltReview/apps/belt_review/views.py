# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Book, Review, Author


# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')


def register(request):
    results = User.objects.registerVal(request.POST)
    if not results['status']:
        for error in results['errors']:
            messages.error(request, error)
    else:
        messages.success(request, 'User created, please login.')

    return redirect('/')


def login(request):
    results = User.objects.loginVal(request.POST)
    if not results['status']:
        for error in results['errors']:
            messages.error(request, error)
    else:
        request.session['id'] = results['user'].id
        return redirect('/books')
    return redirect('/')


def logout(request):
    request.session.clear()
    messages.success(request, 'Logged Out')
    return redirect('/')


def books(request):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')
    user = User.objects.get(id=request.session.get('id'))
    books = Book.objects.all()
    reviews = Review.objects.all()
    context = {
        'user': user,
        'books': books,
        'reviews': reviews,
    }
    return render(request, 'belt_review/index.html', context)


def booksAdd(request):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')
    user = User.objects.get(id=request.session.get('id'))
    authors = Author.objects.all()
    context = {
        'user': user,
        'authors': authors,
    }
    return render(request, 'belt_review/booksAdd.html')


def addBook(request):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')
    results = Book.objects.addBookVal(request.POST)
    if not results['status']:
        for error in results['errors']:
            messages.error(request, error)
    else:
        messages.success(request, 'Book Successfully Added.')
    print results
    return render(request, '/books/'+str(results.Book['id']))


def booksView(request):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')
    pass


def userProfile(request):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')
    pass


def addDeleteReview(request):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')
    pass
