from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
	url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    url(r'^contact/', 'posts.views.contact', name='contact'),
    url(r'^about/', 'posts.views.about', name='about'),
	url(r'^work/', 'posts.views.work', name='work'),
	url(r'^Home/', 'posts.views.home', name='home'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
