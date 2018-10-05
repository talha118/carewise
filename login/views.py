# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from django.http.response import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from login.utils import trusted_authentication_tableau

def home_view(request):
    return render(request, 'index.html', locals())

@api_view(['POST'])
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.data['username']
        password = request.data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse(status=200)
    else:
        return HttpResponseBadRequest('invalid credentials')
#     return render_to_response('login.html', context_instance=RequestContext(request))


@login_required
def main_page(request):
    response_url = trusted_authentication_tableau(request.user.requested_view, request.user.username)
    return render(request, 'main.html', locals())

def logout_view(request):
    logout(request)
    return redirect('home')

