#coding: utf-8

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


def index(request):
    question_list = Question.objects.all()
    return  render(request, 'micq/index.html', {'question_list': question_list})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(reverse('login', args=[]))
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


def question_detail(request, pk):

    question = Question.objects.get(pk=pk)
    answer_form = AnswerForm({'question': question})

    answer_list = Answer.objects.filter(question=question)
    tag_list = Tag.objects.filter(question=question)
    question_comment_list = Comment.objects.filter(question__pk=pk)
    answer_comment_list = Comment.objects.filter(answer__question__pk=pk)


    return render(request, 'micq/question_detail.html', locals())


@login_required()
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form is not None and form.is_valid():
            question = Question(title=form.cleaned_data['title'],
                             body=form.cleaned_data['body'],
                             user=request.user)
            question.save()
            #使用add()方法增加多对多关系的记录
            tags = Tag.objects.create(tag=form.cleaned_data['tags'])
            question.tags.add(tags)
            return render(request, 'micq/question_detail.html', locals())
    else:
        form = QuestionForm()
    return render(request, 'micq/create_question.html',{'form':form})

@login_required()
def question_delete(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except:
        return render(request, 'micq/fail.html', {'error':'记录不存在或已被删除。'})
    question.delete()
    return HttpResponseRedirect(reverse('index', args=[]))

@login_required()
def question_update(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except:
        return render(request, 'micq/fail.html', {'error':'记录不存在或已被删除。'})
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save
            return render(request, 'micq/create_question.html', locals())


def create_answer(request):
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form is not None and answer_form.is_valid():
            answer = Answer.objects.create(body=answer_form.cleaned_data['body'],
                                           question=answer_form.cleaned_data['question'],
                                           user=request.user)
            answer.save()
















