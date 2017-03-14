from django.conf.urls import include, url 
from django.contrib import admin
from login.views import register,mylogin,changepassword,mylogout
admin.autodiscover()

urlpatterns = [
	url(r'^login/$',mylogin),
	url(r'^register/$',register),
	url(r'^changepassword/(?P<username>\w+)/$',changepassword),
	url(r'^logout/$',mylogout),
	
]