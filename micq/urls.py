from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'micq.views.index', name='index'),
    url(r'^register/$', 'micq.views.register', name='register'),
    url(r'^login/$', 'micq.views.login', name='login'),
    url(r'^logout/$', 'micq.views.logout', name='logout'),
    url(r'^question/(?P<pk>\d+)/$', 'micq.views.question_detail', name='question_detail'),
    url(r'question/add/$', 'micq.views.create_question', name='create_question'),
    url(r'question/(?P<pk>\d+)/delete/$', 'micq.views.question_delete', name='question_delete'),
    url(r'question/(?P<pk>\d+)/update/$', 'micq.views.question_update', name='question_update'),
    url(r'answer/add/$', 'micq.views.create_answer', name='create_answer'),
]
