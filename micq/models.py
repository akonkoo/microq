# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from django.core.urlresolvers import reverse


class UserManager(BaseUserManager):
    '''通过邮箱，密码创建用户'''

    def create_user(self, email, username, password=None, **kwargs):
        if not email:
            raise ValueError(u'用户必须要有邮箱')

        user = self.model(
            email=UserManager.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        if kwargs:
            if kwargs.get('sex', None): user.sex = kwargs['sex']
            if kwargs.get('is_active', None): user.is_active = kwargs['is_active']
            if kwargs.get('uid', None): user.uid = kwargs['uid']
            if kwargs.get('token', None): user.token = kwargs['token']
            if kwargs.get('url', None): user.url = kwargs['url']
            if kwargs.get('desc', None): user.desc = kwargs['desc']
            if kwargs.get('avatar', None): user.avatar = kwargs['avatar']

        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email,
                                password=password,
                                username=username,
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    '''扩展User'''
    # SEX_CHOICES = (('M', '男'),('F', '女'))
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=50, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    sex = models.CharField(choices=(('M', '男'), ('F', '女')), default='M', max_length=5)
    url = models.URLField(null=True, blank=True)
    desc = models.CharField(max_length=2000, null=True, blank=True)
    avatar = models.CharField(max_length=500, null=True, blank=True)
    token = models.CharField(max_length=500, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = '用户'


class CustomAuth(object):
    """自定义用户验证"""
    def authenticate(self, email=None, password=None):
        try:
            user = MyUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = MyUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except MyUser.DoesNotExist:
            return None


class Tag(models.Model):
    tag = models.CharField('标签',max_length=100)

    def __unicode__(self):
        return self.tag

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Question(models.Model):
    title = models.CharField('标题', max_length=150)
    body = models.TextField('问题内容')
    created = models.DateTimeField('创建时间', auto_now_add=True)
    modified = models.DateTimeField('修改时间', auto_now=True)

    user = models.ForeignKey(MyUser, verbose_name='创建者')
    tags = models.ManyToManyField(Tag, verbose_name='标签')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题'
        ordering = ['-created']


class Answer(models.Model):
    body = models.TextField('答案内容')
    created = models.DateTimeField('创建时间', auto_now_add=True)
    modified = models.DateTimeField('修改时间', auto_now=True)
    count = models.IntegerField('计数', default=0,null=True)

    user = models.ForeignKey(MyUser, verbose_name='创建者')
    question = models.ForeignKey(Question, blank=True, null=True, verbose_name='问题')

    def __unicode__(self):
        return self.body

    class Meta:
        verbose_name = '答案'
        verbose_name_plural = '答案'
        ordering = ['-created']


class Comment(models.Model):
    body = models.CharField('评论内容', max_length=500)

    user = models.ForeignKey(MyUser, verbose_name='创建者')
    question = models.ForeignKey(Question, blank=True, null=True, verbose_name='问题')
    answer = models.ForeignKey(Answer, blank=True, null=True, verbose_name='答案')

    def __unicode__(self):
        return self.body

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'









