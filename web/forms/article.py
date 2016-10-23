#!/usr/bin/env python
#-*-coding:utf-8-*-

from django import forms
class HrefPublish(forms.Form):
    category_choice = (
        (1, u'42区'),
        (2, u'段子'),
        (3, u'图片'),
        (4, u'挨踢1024'),
        (5, u'你问我答'),
    )
    href = forms.CharField(max_length=100,min_length=5,
                            error_messages={'required': 'the title can not be null','min_length': 'can not less than 5 charts','max_length':'can not less than 5 charts'},
                            widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'http://','id':"articlehref"}))

    title = forms.CharField(min_length=5,error_messages={'required': 'the title can not be null','min_length': 'can not less than 5 charts','max_length': 'can not less than 5 charts'},
                            widget=forms.TextInput(attrs={'class': "form-control",'id':'title'}))

    summary = forms.CharField(required=False,max_length=256,
                           widget=forms.widgets.Textarea(attrs={'class': "form-control no-radius", 'rows': 3,'id':'summary'}))

    category = forms.IntegerField(widget=forms.widgets.Select(choices=category_choice,
                                                                  attrs={'class': "form-control"}))

class PicturePublish(forms.Form):
    category_choice = (
        (3, u'图片'),
        (5, u'你问我答'),
    )
    img = forms.ImageField(error_messages={'required': 'the img can not be null'})
    title = forms.CharField(required=False,max_length=256,
                           widget=forms.widgets.Textarea(attrs={'class': "form-control no-radius", 'rows': 3}))

    category = forms.IntegerField(widget=forms.widgets.Select(choices=category_choice,
                                                                  attrs={'class': "form-control"}))

class EpisodePublish(forms.Form):
        category_choice = (
            (2, u'段子'),
            (5, u'你问我答'),
        )
        title = forms.CharField(required=False,max_length=256,
                           widget=forms.widgets.Textarea(attrs={'class': "form-control no-radius", 'placeholder': 'the limit is 128 words', 'rows': 3}))
        category = forms.IntegerField(widget=forms.widgets.Select(choices=category_choice,
                                                                  attrs={'class': "form-control"}))
