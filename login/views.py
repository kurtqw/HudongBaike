from django.shortcuts import render_to_response
from form import RegisterForm,LoginForm,ChangepwdForm
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from login.models import UserProfile
def mylogin(request):
	error = []
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			username = data['username']
			password = data['password']
			if login_validate(request,username,password):
				#return render_to_response('welcome.html',{'user':username})
				return HttpResponseRedirect('/')
			else:
				error.append('Please input the correct password')
		else:
			error.append('Please input both username and password')
	else:
		form = LoginForm()
	return render_to_response('login.html',{'error':error,'form':form})


def login_validate(request,username,password):
	rtvalue = False
	user = authenticate(username=username,password=password)
	if user is not None:
		if user.is_active:
			auth_login(request,user)
			return True
	return rtvalue


def register(request):
	error=[]
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			username = data['username']
			email = data['email']
			password = data['password']
			password2= data['password2']
			if not User.objects.all().filter(username=username):
				if form.pwd_validate(password, password2):
					user = User.objects.create_user(username, email, password)
					user.save()
					login_validate(request,username,password)
					#return render_to_response('welcome.html',{'user':username})
					return HttpResponseRedirect('/')
				else:
					error.append('Please input the same password')
			else:
				error.append('The username has existed,please change your username')
	else:
		form = RegisterForm()	
	return render_to_response('register.html',{'form':form,'error':error})

def mylogout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')

def changepassword(request,username):
	error = []
	if request.method == 'POST':
		form = ChangepwdForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(username=username,password=data['old_pwd'])
			if user is not None:
				if data['new_pwd']==data['new_pwd2']:
					newuser = User.objects.get(username__exact=username)
					newuser.set_password(data['new_pwd'])
					newuser.save()
					return HttpResponseRedirect('/login/login/')
				else:
					error.append('Please input the same password')
			else:
				error.append('Please correct the old password')
		else:
			error.append('Please input the required domain')
	else:
		form = ChangepwdForm()
	return render_to_response('changepassword.html',{'form':form,'error':error})


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

