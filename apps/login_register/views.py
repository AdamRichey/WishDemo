# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib import messages

from .models import *

def index(request): #Index Page For Login
    return render(request, 'login_register/index.html')

def register(request): #Validations For Registration Credentials
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

def login(request): #Validations For Login Credentials
    lerrors = User.objects.lvalidator(request.POST)
    if len(lerrors):
        for lerror in lerrors:
            messages.error(request, lerror)
        return redirect('/')
    else:
        name=request.POST['lname']
        request.session['user']=name
        return redirect('/welcome')
        
def logout(request): #Logout/Clearing Session
    request.session['user']=' '
    return redirect('/')

def welcome(request): #Welcome Page Loadout
    if request.session['user']==' ':
        return redirect('/')
    else:
        context={
            'users':User.objects.get(username=request.session['user']),
            'toys':Toy.objects.all().order_by('name'),
            'wishlists':User.objects.get(username=request.session['user']).toy.all()
        }
        return render(request, 'login_register/welcome.html', context)
        
def add(request): #Add Page Render
    return render(request, 'login_register/add.html')


def addnow(request, id): #Adding Toy To Wishlist
    a1=Toy.objects.get(id=id)
    a2=User.objects.get(username=request.session['user'])
    a2.toy.add(a1)
    a2.save()
    return redirect('/welcome')

def delete(request, id): #Delete Toy From Wishlist
    a1=Toy.objects.get(id=id)
    a2=User.objects.get(username=request.session['user'])
    a2.toy.remove(a1)
    a2.save()
    return redirect('/welcome')

def create(request): #Create New Toy
    user=User.objects.get(username=request.session['user'])
    Toy.objects.create(name=request.POST['name'], added_by=user.name)
    return redirect('/welcome')

def info(request, id): #Render Toy
    context={
        'user':User.objects.get(username=request.session['user']).name,
        'toy':Toy.objects.get(id=id),
    }
    return render(request, 'login_register/info.html', context)

def update(request, id): #Update Toy Name
    a1=Toy.objects.get(id=id)
    a1.name=request.POST['name']
    a1.save()
    return redirect('/welcome')

def deletetotal(request, id): #Delete Toy
    a1=Toy.objects.get(id=id)
    Toy.delete(a1)
    return redirect('/welcome')


    

