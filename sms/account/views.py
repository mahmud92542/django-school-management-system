from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
#import korlam, dekhbe j username and password ache naki, and login korar jonno login
from django.contrib.auth import authenticate, login, logout
from .forms import *

def register(request):
	if request.method == 'POST':
		forms = UserRegisterForm(request.POST)
		if forms.is_valid():
			username = forms.cleaned_data["username"]
			password = forms.cleaned_data["password"]

			#try case, same name a jate registration korte na pare
			try:
				User.objects.create_user(username=username,password=password)


				return redirect('user_login')
			except:
				errMsg = 'User already exist.'
				context = {'forms':forms, 'errMsg':errMsg}
				return render(request,'register.html',context)

		else:
			context = {'forms':forms}
			return render (request,'register.html',context)

	forms = UserRegisterForm()
	context = {'forms':forms}
	return render (request,'register.html',context)


#Login form

def user_login(request):
	if request.method == 'POST':
		forms = UserLoginForm(request.POST)
		if forms.is_valid():
			username = forms.cleaned_data['username']
			password = forms.cleaned_data['password']

			user = authenticate(username=username,password=password)
			if user:
				login(request, user)
				return redirect('dashboard')
			else:
				errMsg = "User name or Password doesn't found"
				context = {'forms':forms, 'errMsg':errMsg}
				return render(request,'user_login.html',context)
		else:
			errMsg = "User name or Password does'not found"
			context = {'forms':forms, 'errMsg':forms.errors}
			return render (request,'user_login.html',context)

	forms = UserLoginForm()
	context = {'forms':forms}
	return render (request,'user_login.html',context)

#Logout Form

def user_logout(request):
	logout(request)
	return redirect('home')

def SchoolInfo(request):
	if request.method == 'POST':
		forms = SchoolInfoForm(request.POST)
		if forms.is_valid():
			forms.save()
			success = "Information Saved."
			context = {'msg':success, 'forms':forms}
			return redirect ('school-info')
		else:
			forms = SchoolInfoForm()
			error = "Information didn't save."
			context = {'msg':error, 'forms':forms}
			return render(request,'SchoolInfo.html',context)
	forms = SchoolInfoForm()
	context = {'forms':forms}
	return render(request,'SchoolInfo.html',context)

def StudentFees(request):
	if request.method == 'POST':
		forms = StudentFeesForm(request.POST)
		if forms.is_valid():
			forms.save()
			success = "Information Saved."
			context = {'msg':success, 'forms':forms}
			return redirect ('student-fees')
		else:
			forms = StudentFeesForm()
			error = "Information didn't save."
			context = {'msg':error, 'forms':forms}
			return render(request,'StudentFees.html',context)
	forms = StudentFeesForm()
	context = {'forms':forms}
	return render(request,'StudentFees.html',context)