#!/usr/bin/env python
#-*-coding:utf-8-*-

import json
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from web.forms import login as loginForm

def log_in(request):
    ret_data = {'status':1}
    loginInfo = loginForm.userInfo(request.POST)
    if request.method == 'POST':
        if loginInfo.is_valid():
            data = loginInfo.clean()
            user = authenticate(**data)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                error_msg = loginInfo.errors.as_data()
                renderHtml = render(request,'include/login.html',{'obj':loginInfo,'error_messages':error_msg})
    else:
        renderHtml = render(request,'include/login.html',{'obj':loginInfo})
    ret_data['htmldata'] = str(renderHtml).split('Content-Type: text/html; charset=utf-8')[1]
    return HttpResponse(json.dumps(ret_data))

def log_out(request):
    logout(request)
    return  HttpResponseRedirect('/')