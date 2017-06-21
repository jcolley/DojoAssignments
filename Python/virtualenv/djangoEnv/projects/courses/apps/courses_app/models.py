# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# All them models, yo:
class Courses(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name + " - " + self.description + " - " + self.category
