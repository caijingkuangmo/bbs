#!/usr/bin/env python
#-*-coding:utf-8-*-


from django.shortcuts import render,HttpResponse
from web import models

def home(request):
    articles = models.Article.objects.all()
    return render(request, 'home.html',{'articles':articles})

def category(request,categoryId):
    articles = models.Article.objects.filter(category_id=categoryId)
    return render(request, 'home.html',{'articles':articles})
