# coding: utf-8
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
             raise forms.ValidationError(u'密码不正确')
        #assert isinstance(password2, object)
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
