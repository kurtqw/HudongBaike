from django.conf.urls import include, url 
from django.contrib import admin
from chat.views import *
admin.autodiscover()

urlpatterns = [
	url(r'^$',chat),
	url(r'^publish/$',publish),
]