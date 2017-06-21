# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    published_date = models.DateField()
    category = models.TextField()
    in_print = models.BooleanField(default=False)
