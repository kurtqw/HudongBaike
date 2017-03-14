#coding:utf-8
from django.shortcuts import render
from models import *
from form import ChatForm
from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
# Create your views here.

def chat(request):
    List=Chat.objects.all()
    return render(request, 'chat.html',{'List':List})

def publish(request):
	if request.method == 'POST':  
		form = ChatForm(request.POST) 
		if form.is_valid():
			user1=request.POST.get('user')
			content1=request.POST.get('content')
			u1=Chat(user=user1,content=content1)
			u1.save()
			return HttpResponseRedirect('/chat/')
