# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class adsDetails(models.Model):
    client_id=models.ForeignKey(User, unique=True,on_delete=models.CASCADE)
    header = models.CharField('Header text', max_length=300,default="",blank= True)
    left_top = models.CharField('Ad-1: Top Left', max_length=200,default="",blank= True)
    left_bottom = models.CharField('Ad-2: Bottom Left', max_length=200,default="",blank= True)
    right_top = models.CharField('Ad-3: Top Right', max_length=200,default="",blank= True)
    right_bottom = models.CharField('Ad-4: Bottom Right', max_length=200,default="",blank= True)
    footer = models.CharField('Footer Text', max_length=300,default="",blank= True)
    update_flag = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return str(self.client_id)

class clientDetails(models.Model):
    client_id = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    client_name = models.CharField('Name', max_length=300, default="", blank=True)
    business =(
			    ('Mall', 'Mall'),
			    ('Theatre', 'Theatre'),
			    ('RE', 'Real Estate'),
			    ('Retail', 'Retail'),
    )
    client_business = models.CharField('Business', max_length=100, choices=business, default="", blank=True)
    client_contact = models.IntegerField('Contact number', max_length=15, default="", blank=True, null=True)
    client_email = models.CharField('Email', max_length=50, default="", blank=True)
    client_address = models.CharField('Address', max_length=150, default="", blank=True)
    client_locality = models.CharField('Locality', max_length=50, default="", blank=True)
    client_city = models.CharField('City', max_length=50, default="", blank=True)
    client_state = models.CharField('State', max_length=30, default="", blank=True)
    client_country = models.CharField('Country', max_length=30, default="", blank=True)

    def __str__(self):
        return str(self.client_id)