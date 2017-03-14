# coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from form import ArticleForm,SearchForm
from models import Article
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User 
from login.models import UserProfile
# Create your views here.

def new(request):
	return render(request, 'new.html')

def success(request):
	return render(request, 'success.html')

def failure(request):
	return render(request, 'failure.html')

def failure1(request):
	return render(request, 'failure1.html')

def default(request):
	return render(request, 'default.html')


def templates(request):
	return render(request, 'templates.html')

def result(request):
	if request.method == 'POST':  
		form = SearchForm(request.POST) 
		if form.is_valid():
			title = request.POST.get('title')
			form1 = ArticleForm
			title1=title
			if Article.objects.all().filter(title=title):
				content1=Article.objects.get(title=title).content
				user1=Article.objects.get(title=title).user
				return render_to_response('result.html',{'title1':title1,'user1':user1,'content1':content1})
				
			else:
				return HttpResponseRedirect('/article/default/')
							
		



def savearticle(request):
	error=[]
	if request.method == 'POST':  
		form = ArticleForm(request.POST) 
		if form.is_valid():
			title = request.POST.get('title')
		 	content = request.POST.get('content')
		 	user = request.POST.get('user')

		 	username = request.user

			if not Article.objects.all().filter(title=title):
						
				u1=Article(title=title,content=content,user=user)
				u1.save()

				#用户扩展信息 profile  
				 
				user1=UserProfile.objects.get(user=username)
				user1.point=user1.point+1
				user1.save()
				return HttpResponseRedirect('/article/success/')

							
			else:
				return HttpResponseRedirect('/article/failure/')
		

def change1(request):
	if request.method == 'POST':  
		form = ArticleForm(request.POST) 
		if form.is_valid():
			
			title1 = request.POST.get('title')
		 	content1 = request.POST.get('content')
		 	user1 = request.POST.get('user')
			if not Article.objects.all().filter(title=title1):
				return HttpResponseRedirect('/article/failure1/')
			else:
			 	username = request.user

				u1=Article.objects.get(title=title1)
							
				u1.content=content1
				u1.user=user1
				u1.save()

				#用户扩展信息 profile  
				 
				user2=UserProfile.objects.get(user=username)
				user2.point=user2.point+1
				user2.save()

				return render_to_response('result.html',{'title1':title1,'user1':user1,'content1':content1})


def change(request):
	return render(request, 'change.html')