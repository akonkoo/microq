#coding: utf-8
from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms

from .models import *
from .forms import *


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


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'sex', 'url', 'desc', 'avatar', 'token',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('email', 'username', 'sex', 'url',
        'desc', 'avatar', 'token', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created','user')
    list_filter = ('user', 'tags',)


admin.site.register(MyUser, MyUserAdmin)
admin.site.unregister(Group)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Tag)

