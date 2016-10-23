#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Eva_J'
import json

from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from web import models

def getCommentLst(request):
    ret_data = {'status':1}
    title = request.GET.get('title')
    articleObj = models.Article.objects.filter(title=title.strip()).first()
    commentLst = articleObj.comment_set.select_related()
    renderCommentTree =  render(request,'include/commentTree.html',{'commentLst':commentLst})
    ret_data['commentTree'] = str(renderCommentTree).split('Content-Type: text/html; charset=utf-8')[1]
    return HttpResponse(json.dumps(ret_data))

def dealwithThumb(request):
    ret_data = {'status':1}
    title = request.GET.get('title')
    articleObj = models.Article.objects.filter(title=title.strip()).first()
    thumbupObj = articleObj.thumbup_set.filter(user_id=request.user.userprofile.id)
    if thumbupObj:
        thumbupObj.delete()
    else:
        obj = models.ThumbUp(article=articleObj,user=request.user.userprofile)
        obj.save()
    return HttpResponse(json.dumps(ret_data))

def commentReply(request):
    linkid=0
    ret_data = {'status':1}
    articleObj = models.Article.objects.filter(title=request.POST.get('title').strip()).first()
    if request.POST.get('linkid'):
        linkid = int(request.POST.get('linkid'))
    print request.POST
    try:
        if linkid:
            obj = models.Comment(article=articleObj,user=request.user.userprofile,
                                 comment=request.POST.get('comment').strip(),
                                 parent_comment_id=linkid)
        else:
            obj = models.Comment(article=articleObj,user=request.user.userprofile,
                                 comment=request.POST.get('comment').strip(),
                                 parent_comment_id=request.POST.get('linkid'))
        obj.save()
    except Exception as e:
        print 'error:',e
    return HttpResponse(json.dumps(ret_data))