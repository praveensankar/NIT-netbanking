from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<username>[A-Za-z0-9]+)/dashboard/$', views.dashboard, name='dashboard'),
    url(r'^(?P<username>[A-Za-z0-9]+)/transfer/$', views.transfer, name='transfer'),
    url(r'^postlogin/$', views.postlogin, name='postlogin'),
    url(r'^posttransfer/$', views.posttransfer, name='posttransfer'),
    url(r'^postregister/$', views.postregister, name='postregister'),
]


