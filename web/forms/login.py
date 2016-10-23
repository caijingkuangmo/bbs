#!/usr/bin/env python
#-*-coding:utf-8-*-

from django import forms

class userInfo(forms.Form):
    username = forms.CharField(error_messages={'required': 'Username can not be null.'},
                               widget=forms.TextInput(attrs={ 'placeholder': 'userName','class':'form-control input-style loginInput','id':"inputUser"}))
    password = forms.CharField(error_messages={'required': 'Password can not be null.'},
                               widget=forms.PasswordInput(attrs={ 'placeholder': 'password','class':'form-control input-style loginInput','id':"inputPassword"}))
