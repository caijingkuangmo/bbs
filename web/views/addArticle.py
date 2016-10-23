#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Eva_J'
import os
import json
import urllib2

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from web.forms import article
from web import models

def publish(request,saveType):
    print request.method,request.FILES,saveType,request.POST
    formMap = {'href':article.HrefPublish,'episode':article.EpisodePublish,'picture':article.PicturePublish}
    ret_data = {'status':1}
    obj = formMap[saveType](request.POST,request.FILES)
    if request.method == 'POST':
        if obj.is_valid():
            data = obj.clean()
            authorid = request.user.userprofile.id
            articleObj = models.Article(title=data['title'],author_id=authorid,category_id=int(data['category']))
            articleObj.save()
            if saveType == 'href':
                Obj = models.ArticleHref(articlehref=data['href'],summary=data['summary'],article=articleObj)
                Obj.save()
            elif saveType == 'picture':
                newImgPath = uploadImg(authorid,request.FILES['img'])
                data['img'] = newImgPath
                Obj = models.ArticlePicture(img=data['img'],article=articleObj)
                Obj.save()
            return HttpResponseRedirect('/')
        else:
            error_msg = obj.errors.as_data()
            renderHtml =  render(request,'include/'+saveType+'Publish.html',{saveType:obj,'errors':error_msg})
    else:
        renderHtml = render(request,'include/'+saveType+'Publish.html',{saveType:obj})
    ret_data['htmldata'] = str(renderHtml).split('Content-Type: text/html; charset=utf-8')[1]
    return HttpResponse(json.dumps(ret_data))

def geturl(request):
    ret_data = {'status':1}
    url = request.GET.get('url')
    print url
    try:
        response = urllib2.urlopen(url, timeout=10)
        title =  response.read().split('<title>')[1].split('</title>')[0]
        ret_data['gettitle'] = title
    except Exception,e:
        ret_data['status'] = 0
        ret_data['error'] = e
    return HttpResponse(json.dumps(ret_data))

def add(request):
    ret_data = {'status':1}
    if 'href' in request.POST.keys():
        saveType='href'
    elif request.FILES:
        saveType='picture'
    else:
        saveType='episode'
    return publish(request,saveType)


def uploadImg(authorid,f):
    base_image_upload_path = 'statics/uploads'
    userpath = '%s/%s'%(base_image_upload_path,authorid)
    if not os.path.exists(userpath):
        os.mkdir(userpath)
    with open('%s/%s'%(userpath,f.name),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return '/static/uploads/%s/%s'%(authorid,f.name)