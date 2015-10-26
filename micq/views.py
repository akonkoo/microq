#coding: utf-8

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

from django.views.generic.edit import UpdateView


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
    try:
        question = Question.objects.get(pk=pk)
    except:
        return HttpResponseRedirect('micq/fail.html')

    answer_form = AnswerForm()

    answer_list = Answer.objects.filter(question=question)
    #tag_list = Tag.objects.filter(question=question)
    question_comment_list = Comment.objects.filter(question__pk=pk)
    answer_comment_list = Comment.objects.filter(answer__question__pk=pk)
    c_q = False
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

            #使用split方法拆分用户输入的tags,注意create的类型
            #使用add()方法增加多对多关系的记录
            tag = form.cleaned_data['tags']
            for item in tag.split(' '):
                tags = Tag.objects.create(tag=item)
                question.tags.add(tags)
            return HttpResponseRedirect(reverse('question_detail', args=[question.pk]))
    else:
        form = QuestionForm()
    return render(request, 'micq/create_question.html', {'form': form})


@login_required()
def question_delete(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except:
        return HttpResponseRedirect('micq/fail.html')
    if question.user == request.user:
        question.delete()
    return redirect('index')


@login_required()
def question_update(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except:
        return render(request, 'mciq/fial.html')

    if question.user == request.user:

        if request.method == 'POST':
            form = QuestionForm(request.POST or None, instance=question)
        
            if form.is_valid():
                f = form.save(commit=False)

                question.tags.clear()
                tag = form.cleaned_data['tags']
                for item in tag.split(' '):
                    tags = Tag.objects.create(tag=item)
                    question.tags.add(tags)

                f.save()
            return HttpResponseRedirect(reverse('question_detail', args=[question.pk]))
        else:
            form = QuestionForm(instance=question)
            

        return render(request, 'micq/create_question.html', {'form': form})


@login_required()
def create_answer(request, pk):
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form is not None and answer_form.is_valid():

            answer = Answer.objects.create(body=answer_form.cleaned_data['body'],
                                            user=request.user)
            answer.save()

            #增加对应ForeigKey数据
            answer.question = Question.objects.get(pk=pk)
            answer.save()        
        return HttpResponseRedirect(reverse('question_detail', args=[pk]))


def answer_detail(request, pk, id):
    question = Question.objects.get(pk=pk)
    answer = Answer.objects.get(id=id)
    return render(request, 'micq/answer_detail.html', locals())


@login_required
def answer_update(request, pk, id):
    question = Question.objects.get(pk=pk)
    answer = Answer.objects.get(id=id)
    if answer.user == request.user:
        if request.method == 'POST':
            form = AnswerForm(request.POST or None, instance=answer)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse('question_detail', args=[pk]))
        else:
            form = AnswerForm(instance=answer)
        return render(request, 'micq/answer_detail.html', {'question':question,
                                    'form': form,
                                    'answer_update': True})


@login_required
def answer_delete(request, pk, id):
    question = Question.objects.get(pk=pk)
    answer = Answer.objects.get(id=id)
    if answer.user == request.user:
        answer.delete()
        return HttpResponseRedirect(reverse('question_detail', args=[pk])) 


def create_comment(request, pk):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form is not None and comment_form.is_valid():
            comment = Comment.objects.create(body=comment_form.cleaned_data['bdoy'],
                                            user=request.user)
            comment.save()
            comment.question = Question.objects.get(pk=pk)
            comment.save()
        return HttpResponseRedirect(reverse('question_detail', args=[pk]))
    else:
        comment_form = CommentForm()
        c_q = True
        return HttpResponseRedirect(reverse('question_detail', args=[pk])) 



        
            















