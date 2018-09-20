# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class adsDetails(models.Model):
    client_id=models.ForeignKey(User, unique=True,on_delete=models.CASCADE)
    header = models.CharField('Full Name', max_length=300)
    left_top = models.CharField('Full Name', max_length=200)
    left_bottom = models.CharField('Full Name', max_length=200)
    right_top = models.CharField('Full Name', max_length=200)
    right_bottom = models.CharField('Full Name', max_length=200)
    footer = models.CharField('Full Name', max_length=300)

    def __str__(self):
        return str(self.client_id)
