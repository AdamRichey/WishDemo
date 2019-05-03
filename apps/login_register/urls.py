from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^welcome$', views.welcome),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^addnow/(?P<id>[0-9]{2}$)', views.addnow),
    url(r'^delete/(?P<id>[0-9]{2}$)', views.delete),
    url(r'^info/(?P<id>[0-9]{2}$)', views.info),
    url(r'^addnow/(?P<id>[0-9]$)', views.addnow),
    url(r'^delete/(?P<id>[0-9]$)', views.delete),
    url(r'^deletetotal/(?P<id>[0-9]{2}$)', views.deletetotal),
    url(r'^update/(?P<id>[0-9]$)', views.update),
    url(r'^update/(?P<id>[0-9]{2}$)', views.update),
    url(r'^deletetotal/(?P<id>[0-9]$)', views.deletetotal),
    url(r'^info/(?P<id>[0-9]$)', views.info),
  ]
