# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40, default="socks")
    description = models.TextField(default="white socks")
    weight = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    category = models.CharField(max_length=40, default="food")
