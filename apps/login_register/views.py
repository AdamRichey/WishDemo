# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib import messages

from .models import *

def index(request):
    return render(request, 'login_register/index.html')

def welcome(request):
    if request.session['user']==' ':
        return redirect('/')
    else:
        context={
            'users':User.objects.get(username=request.session['user']),
            'toys':Toy.objects.all(),
            'wishlists':User.objects.get(username=request.session['user']).toy.all()
        }
        return render(request, 'login_register/welcome.html', context)

def register(request):
    errors = User.objects.rvalidator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect ('/')
    else:
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        User.objects.create(name=name, username=username, password=password)
        request.session['user']=username
        return redirect('/welcome')
        

def login(request):
    lerrors = User.objects.lvalidator(request.POST)
    if len(lerrors):
        for lerror in lerrors:
            messages.error(request, lerror)
        return redirect('/')
    else:
        name=request.POST['lname']
        request.session['user']=name
        return redirect('/welcome')
def logout(request):
    request.session['user']=' '
    return redirect('/')

def add(request):
    return render(request, 'login_register/add.html')

def create(request):
    user=User.objects.get(username=request.session['user'])
    Toy.objects.create(name=request.POST['name'], added_by=user.name)
    return redirect('/welcome')

def addnow(request, id):
    a1=Toy.objects.get(id=id)
    a2=user=User.objects.get(username=request.session['user'])
    a2.toy.add(a1)
    a2.save()
    return redirect('/welcome')

def delete(request, id):
    a1=Toy.objects.get(id=id)
    a2=user=User.objects.get(username=request.session['user'])
    a2.toy.remove(a1)
    a2.save()
    return redirect('/welcome')

def info(request, id):
    context={
        'toy':Toy.objects.get(id=id)
    }
    return render(request, 'login_register/info.html', context)
    

# Create your views here.
