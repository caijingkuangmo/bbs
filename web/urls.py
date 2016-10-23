#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Eva_J'
from django.conf.urls import include, url

from views import auth
from views import index
from views import addArticle
from views import commentManage
urlpatterns = [
    url(r'^login/$', auth.log_in, name='login'),
    url(r'^logout/$', auth.log_out, name='logout'),
    url(r'^category/(\d+)/$', index.category, name='category'),
    url(r'^publish/([a-z]+)/$', addArticle.publish,name='publish'),
    url(r'^geturl/$', addArticle.geturl,name='geturl'),
    url(r'^getCommentLst/$', commentManage.getCommentLst,name='getCommentLst'),
    url(r'^commentThumb/$', commentManage.dealwithThumb),
    url(r'^commentReply/$', commentManage.commentReply),
    url(r'^add/$', addArticle.add,name='add'),
    url(r'^$', index.home,name='home'),
]
