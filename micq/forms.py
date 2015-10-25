# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

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
    #question = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Answer
        fields = ['body']








