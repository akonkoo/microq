# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import *


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'username')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
             raise forms.ValidationError(u'两次密码输入不同')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'username', 'sex', 'url',
            'desc', 'avatar', 'token','is_active', 'is_admin')

    def clean_password(self):
        return self.initial['password']


class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=150)
    body = forms.CharField(widget=forms.Textarea)
    tags = forms.CharField(max_length=50)

    class Meta:
        model = Question
        fields = ['title', 'body', 'tags']



class AnswerForm(forms.ModelForm):
    body = forms.CharField(label='回答', widget=forms.Textarea)

    class Meta:
        model = Answer
        fields = ['body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['body']


class UserForm(forms.ModelForm):
    url = forms.URLField(label='微博')
    desc = forms.CharField(label='个人简介', widget=forms.Textarea)

    def clean_url(self):
        url = self.cleaned_data.get('url')
        url = 'http://' + url
        return url

    class Meta:
        model = MyUser
        fields = ['username', 'sex', 'url', 'desc']


class SetPasswordForm(forms.Form):
    error_messages = {
    'password_mismatch': u"两次密码不一致"
    }
    new_password1 = forms.CharField(label="新密码",
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="确认密码",
                                    widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                            self.error_messages['password_mismatch'],
                            code='password_mismatch')

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user


class PasswordChangeForm(SetPasswordForm):
    error_messages = dict(SetPasswordForm.error_messages, **{
                        'password_incorrect':u"旧密码不正确，请重新输入"
                        })
    old_password = forms.CharField(label="旧密码",
                                    widget=forms.PasswordInput)
    def clean_old_password(self):
        #验证旧密码
        old_password = self.cleaned_data['old_password']
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                        self.error_messages['password_incorrect'],
                        code='password_incorrect')
        return old_password


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)

    def send_email(self, subject_template_name, email_template_name, 
                    context, from_email, to_email, html_email_template_name=None):
        subject = loader.render_to_string(subject_template_name,
                                        context)
        #Email Subject 不能有换行符
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)
        email_message = EmailMultiAlternatives(subject, body,
                                            from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')            
        email_message.send()

    def get_users(self, email):
        #判断是否活跃用户
        active_users = get_user_model()._default_manager.filter(
                        email__iexact=email, is_active=True)
        return (u for u in active_users if u.has_usable_password())

    def save(self, domain_override=None,
            subject_template_name='micq/email/password_reset_subject.txt',
            email_template_name='micq/email/password_reset_email.html',
            use_https=False,
            token_generator=default_token_generator,
            from_email=None, request=None,
            html_email_template_name=None):
        #生成一个一次性使用唯一的链接，重置密码，并发送至用户

        email = self.cleaned_data['email']

        for user in self.get_users(email):
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
                
            context = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                #将user.pk解析成字符串，再编码以便在URL中使用
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                #生成加密验证数据
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
            }

            self.send_email(subject_template_name, 
                            email_template_name, context, from_email, user.email,
                            html_email_template_name=html_email_template_name)








