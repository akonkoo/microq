from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'micq.views.index', name='index'),
    url(r'^register/$', 'micq.views.register', name='register'),
    url(r'^login/$', 'micq.views.login', name='login'),
    url(r'^logout/$', 'micq.views.logout', name='logout'),
]
