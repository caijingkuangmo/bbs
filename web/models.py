#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    #content=models.TextField(u"内容") #不定长可扩展类型TextField
    publish_date = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=False)
    priority = models.IntegerField(u"优先级",default=1000) #区分文章指定等位置

    author = models.ForeignKey('UserProfile')
    category = models.ForeignKey('Category',verbose_name=u"板块") #verbose_name如果是关联关系需要指定默认参数，如果只是普通字段，放在第一个位置即可

    def __unicode__(self):
        return "<%s, author:%s>"%(self.title,self.author)

class ArticleHref(models.Model):
    articlehref = models.CharField(max_length=255,default='http://www.cnblogs.com/Eva_J')
    summary = models.CharField(max_length=255,blank=True,null=True)
    img = models.ImageField(upload_to="uploads",blank=True,null=True)
    article = models.OneToOneField('Article')

class ArticlePicture(models.Model):
    img = models.ImageField(upload_to="uploads")
    article = models.OneToOneField('Article')

class Category(models.Model):
    name = models.CharField(max_length=64,unique=True)
    admin = models.ManyToManyField('UserProfile')
    def __unicode__(self):
        return self.name

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    article = models.ForeignKey('Article')
    user = models.ForeignKey("UserProfile")
    parent_comment = models.ForeignKey('self',related_name='parentCom',blank=True,null=True)#表中字段关联自己表中的另一个字段，必须指定一个related_name不能与本表中的任何字段名相同

    def __unicode__(self):
        return "<%s, user:%s>"%(self.comment,self.user)

class UserGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    groups = models.ManyToManyField('UserGroup')
    def __unicode__(self):
        return self.name

class ThumbUp(models.Model):
    date = models.DateTimeField(auto_now=True)
    article = models.ForeignKey('Article')
    user = models.ForeignKey('UserProfile')

    def __unicode__(self):
        return '<user:%s article:%s>'%(self.user,self.article)