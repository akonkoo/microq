#coding: utf-8

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


@login_required
def index(request):
    question_list = Question.objects.all()
    return  render(request, 'micq/index.html', {'question_list': question_list})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(reverse('index', args=[]))
    else:
        form = UserCreationForm()
    return render(request, 'micq/regist.html', {'form': form})


def login(request):
    errors = []
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        if not request.POST.get('email', ''):
            errors.append(u'请输入邮箱地址')
        if not request.POST.get('password', ''):
            errors.append(u'请输入密码')
        if not errors:
            user = auth.authenticate(email=email, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index', args=[]))
            else:
                errors.append(u'账号和密码不符')
    return render(request, 'micq/login.html', {'errors': errors})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login', args=[]))