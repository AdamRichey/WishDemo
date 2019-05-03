# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def rvalidator(self, data):
        errors = []
        if len(data['name'])<2:
            errors.append('Add your name')
        if  data['name'].isdigit == True:
            errors.append('Invalid Name')
        if User.objects.filter(username=data['username']).count()>0:
            errors.append('User Taken')
        if len(data['password'])<8:
            errors.append('Password is too short')
        for char in data['name']:
            if char.isdigit():
                errors.append('Invalid Username')
        if data['password'] != data['cfpw']:
            errors.append('Unmatched Passwords')
        return errors
    
    def lvalidator(self, data):
        lerrors = []
        if len(data['lname'])<1:
            lerrors.append('Add your username')
        elif User.objects.filter(username=data['lname']).count()<1:
            lerrors.append('User does not exist')
        elif User.objects.get(username=data['lname']).password != data['lpassword']:
            lerrors.append('Invalid Password')
            print User.objects.get(username=data['lname']).password
        return lerrors
        
            

class Toy(models.Model):
    name = models.CharField(max_length=100)
    added_by=models.CharField(max_length=100)
    date_Added = models.DateTimeField(auto_now_add = True)
    objects = UserManager()          

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    toy = models.ManyToManyField(Toy, related_name="users")
    objects = UserManager()

# Create your models here.
