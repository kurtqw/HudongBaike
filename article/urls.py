from django.conf.urls import include, url 
from django.contrib import admin
from article.views import *
admin.autodiscover()

urlpatterns = [
	url(r'^new/$',new),
	url(r'^savearticle/$',savearticle),
	url(r'^success/$',success),
	url(r'^failure/$',failure),
	url(r'^failure1/$',failure1),
	url(r'^default/$',default),
	url(r'^result/$',result),
	url(r'^templates/$',templates),
	url(r'^change/$',change),
	url(r'^change1/$',change1),
]