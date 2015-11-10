#coding: utf-8

from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.response import TemplateResponse
from django.utils.encoding import force_text
from django.utils.http import is_safe_url, urlsafe_base64_decode

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
    try:
        question = Question.objects.get(pk=pk)
    except:
        return HttpResponseRedirect('micq/fail.html')

    answer_list = Answer.objects.filter(question=question)
    question_comment_list = Comment.objects.filter(question__pk=pk)
    answer_comment_list = Comment.objects.filter(answer__question__pk=pk)

    answer_form = AnswerForm()
    comment_form = CommentForm()

    return render(request, 'micq/question_detail.html', locals())

#question
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


#answer
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
        return render(request, 'micq/answer_detail.html', {
                                'question':question,
                                'form': form,
                                'answer_update': True        #修改答案框开关
                                })


@login_required
def answer_delete(request, pk, id):
    question = Question.objects.get(pk=pk)
    answer = Answer.objects.get(id=id)
    if answer.user == request.user:
        answer.delete()
        return HttpResponseRedirect(reverse('question_detail', args=[pk])) 


@login_required
def question_comment_create(request, pk):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form is not None and comment_form.is_valid():
            comment = Comment.objects.create(body=comment_form.cleaned_data['body'],
                                            user=request.user)
            comment.save()
            if comment_q:
                comment.question = Question.objects.get(pk=pk)
            elif comment_a:
                comment.answer = Answer.objects.get(question__pk=pk)
            comment.save()
        return HttpResponseRedirect(reverse('question_detail', args=[pk]))
    else:
        comment_form = CommentForm()
        return render(request, 'micq/question_detail.html', locals())


@login_required
def question_comment_delete(request, pk, id):
    question = Question.objects.get(pk=pk)
    comment = Comment.objects.get(id=id)
    comment.delete()
    return HttpResponseRedirect(reverse('question_detail', args=[pk]))

@login_required
def users(request):
    user = request.user
    question_list = Question.objects.filter(user=user)
    answer_list = Answer.objects.filter(user=user)
    return render(request, 'micq/users.html', locals())


@login_required
def userchange(request):
    user = request.user
    if request.method == "POST":
        form = UserForm(request.method or None, instance=user)
        if form.is_valid():
            form.save()
        return render(request, 'micq/users.html', locals())
    else:
        form = UserForm(instance=user)
    return render(request, 'micq/userchange.html', {'form':form})


@login_required
def password_change(request):
    
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            
            #防止更新密码之后登出会话
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse('users', args=[]))
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'micq/password_change.html', {'form': form})


def password_reset(request, is_admin_site=False,
                    template_name='micq/password_reset_form.html',
                    email_template_name='micq/email/password_reset_email.html',
                    subject_template_name='micq/email/password_reset_subject.txt',
                    password_reset_form=PasswordResetForm,
                    token_generator=default_token_generator,
                    post_reset_redirect=None,
                    from_email=None,
                    current_app=None,
                    extra_context=None,
                    html_email_template_name=None):
    # if post_reset_redirect is None:
    #     post_reset_redirect = reverse('password_reset_done')
    # else:
    #     post_reset_redirect = resolve_url(post_reset_redirect)
    if request.method == 'POST':
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
            }
            if is_admin_site:
                warnings.warn(
                    'django.contrib.auth.views.password_reset()'
                    '的参数is_admin_site'
                    '已取消，将在Django 2.0中删除。',
                    RemovedInDjango20Warning, 3)
                opts = dict(opts,
                domain_override=request.get_host())
            form.save(**opts)
            return HttpResponseRedirect('/password_reset_done/')
    else:
        form = password_reset_form()
        context = {
            'form': form,
            'title': 'Password reset',
        }

    if extra_context is not None:
        context.update(extra_context)
        
    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)


def password_reset_done(request):
    return render(request, 'micq/password_reset_done.html', {
                    'title': 'Password reset sent'})


def password_reset_confirm(request, uidb64=None, token=None,
                            template_name="micq/password_reset_confirm.html",
                            token_generator=default_token_generator,
                            post_reset_redirect=None,
                            current_app=None, extra_context=None):

    UserModel = get_user_model()
    assert uidb64 is not None and token is not None  #check by URLconf

    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_complete')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)

    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        title = 'Enter new password'
        if request.method == 'POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(post_reset_redirect)
        else:
            form = set_password_form(user)
    else:
        validlink = False
        form = None
        title = 'Password reset Unsuccessful'

    context = {
        'form': form,
        'title': title,
        'validlink' : validlink,
    }

    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app
        
    return TempalteResponse(request, template_name, context)


def password_reset_complete(request, 
                            template_name="mciq/password_reset_complete.html",
                            current_app=None, extra_context=None):
    context = {
        'login_url' : resolve_url(settings.LOGIN_URL),
        'title': 'Password reset complete',
    }

    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TempalteResponse(request, template_name, context)

    

        
            















