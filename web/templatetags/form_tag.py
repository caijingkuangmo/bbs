#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime

from django import template

register = template.Library()

@register.simple_tag
def error_message(arg):
    if arg:
        return arg[0][0]
    else:
        return ''

@register.simple_tag
def thumb_user(request,article):
    if article.thumbup_set.filter(user_id=request.user.userprofile.id):
        if article.thumbup_set.filter(user_id=request.user.userprofile.id):
            return 'item-agree-click'
    else:
        return ''

def treeSearch(comment_dic,commentObj):
    for k in comment_dic:
        if k == commentObj.parent_comment:
            comment_dic[k][commentObj] = {}
            return
        else:
            treeSearch(comment_dic[k],commentObj)

def generate_comment_html(sub_comment_dic,marginLeft):
    html = ""
    for k in sub_comment_dic:
       html += "<div class='comment-node'style='margin-left:%spx'><span>%s : </span><span>%s</span><a linkid='%s' onclick='replySon(this)'>[reply]</a></div>"%(marginLeft,k.user.name,k.comment,k.id)
       if  sub_comment_dic[k]:
           html += generate_comment_html(sub_comment_dic[k],marginLeft+20)
    return html

@register.simple_tag
def build_comment_tree(commentList):
    print commentList,'~n*(@.@)*n~'
    comment_dic = {}
    for commentObj in commentList:
        if commentObj.parent_comment is None:
            comment_dic[commentObj]={}
        else:
            treeSearch(comment_dic,commentObj)
    node_html = ''
    for k in comment_dic:
        marginLeft = 0
        node_html +="<div class='comment-node'><span>%s : </span><span>%s</span><a linkid='%s'onclick='replySon(this)'>[reply]</a></div>"%(k.user.name,k.comment,k.id)
        #node_html +="<div class='comment-node'><span>%s : </span><span>%s</span><a linkid='%s'>回复</a></div>"%(k.user.name,k.comment,k.id)
        node_html += generate_comment_html(comment_dic[k],marginLeft+20)
    return node_html


@register.simple_tag
def countTime(commentObj):
    timeNow =  datetime.datetime.now()
    timePublish = commentObj.publish_date
    if timeNow.day == timePublish.day:
        if timeNow.hour == timePublish.hour:
            if timeNow.minute == timePublish.minute:
                return '不足1分钟前'
            else:
                return '%s分钟前'%(timeNow.minute - timePublish.minute)
        else:

            return '%s小时前'%(timeNow.hour - timePublish.hour)
    else:
        return '超过24小时前'






