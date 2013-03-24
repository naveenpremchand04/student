# Create your views here.
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from student.models import student
from django.db.models import Q
from datetime import datetime
#users home page

def newpost(request):
		if request.method == 'POST':
			name= request.POST.get('name')
			sex = request.POST.get('sex')
			age= request.POST.get('age')
			mark1= request.POST.get('mark1')
			mark2= request.POST.get('mark2')
			mark3= request.POST.get('mark3')
			mark4= request.POST.get('mark4')
			mark5= request.POST.get('mark5')
			mark6= request.POST.get('mark6')
			p = student(name=name,sex=sex,age=age,mark1=mark1,mark2=mark2,mark3=mark3,mark4=mark4,mark5=mark5,mark6=mark6)
			p.save()
			return HttpResponseRedirect("/")
		else:
			status = request.GET.get('status')
        		t = get_template('addpost.html')
			if status:
				html = t.render(Context({'message' : "Username already exists"}))
			else:
				html = t.render(Context({'message' : ""}))
			return HttpResponse(html)

def guestpage(request):

	status = request.GET.get('status')
        t = get_template('guest.html')
	try:
	#Retreiving the require posts
		entries = student.objects.all()
	except student.DoesNotExist:
		if status:
				html = t.render(Context({  'entries' : None, 'message' : "User does not exist"}))
		else:
				html = t.render(Context({  'entries' : None, 'message' : ""}))
	else:
		if status:
				html = t.render(Context({  'entries' : entries, 'message' : "User does not exist"}))
		else:
				html = t.render(Context({  'entries' : entries, 'message' : ""}))

	return HttpResponse(html)

def search(request):
		if request.method == 'POST':
			name= request.POST.get('name')
			entries = student.objects.filter(name=name)
			t = get_template('guest.html')
			html = t.render(Context({  'entries' : entries, 'message' : ""}))
			return HttpResponse(html)
		if request.method == 'GET':
			status = request.GET.get('status')
        		t = get_template('search.html')
			html = t.render(Context({  }))
			return HttpResponse(html)
			








	
			
