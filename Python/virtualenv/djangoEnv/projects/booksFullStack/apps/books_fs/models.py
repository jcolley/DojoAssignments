# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Categories(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Authors)
    category = models.ForeignKey(Categories)

    def __str__(self):
        return self.title + " - " + self.author.name + " - " + self.category.category
