#coding: utf-8
from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import *
from .forms import *

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


admin.site.register(MyUser,MyUserAdmin)
admin.site.unregister(Group)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Tag)

