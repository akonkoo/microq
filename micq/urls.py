from django.conf.urls import include, url

from micq.views import *

urlpatterns = [
    url(r'^$', 'micq.views.index', name='index'),
    url(r'^register/$', 'micq.views.register', name='register'),
    url(r'^login/$', 'micq.views.login', name='login'),
    url(r'^logout/$', 'micq.views.logout', name='logout'),
    url(r'^question/(?P<pk>\d+)/$', 'micq.views.question_detail', name='question_detail'),
    url(r'^question/add/$', 'micq.views.create_question', name='create_question'),
    url(r'^question/(?P<pk>\d+)/delete/$', 'micq.views.question_delete', name='question_delete'),
    url(r'^question/(?P<pk>\d+)/update/$', 'micq.views.question_update', name='question_update'),
    url(r'^question/(?P<pk>\d+)/answer/$', 'micq.views.create_answer', name='create_answer'),
   	url(r'^question/(?P<pk>\d+)/answer/(?P<id>\d+)$', 'micq.views.answer_detail', name='answer_detail'),
    url(r'^question/(?P<pk>\d+)/answer/(?P<id>\d+)/update/$', answer_update, name='answer_update'),
    url(r'^question/(?P<pk>\d+)/answer/(?P<id>\d+)/delete/$', answer_delete, name='answer_delete'),
    url(r'^question/(?P<pk>\d+)/comment/$', question_comment_create, name='question_comment_create'),
    url(r'^question/(?P<pk>\d+)/comment/(?P<id>\d+)/delete/$', question_comment_delete, name='question_comment_delete'),
    
    url(r'^users/$', users, name='users'),
    url(r'^users/settings/$', userchange, name='userchange'),
    url(r'^users/password_change/$', password_change, name='password_change'),
    url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_reset_done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, name="password_reset_confirm"),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),
]
