from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *

from django.shortcuts import redirect

#dashboard
@login_required
def dashboard(request):
	return render(request,'academic/dashboard.html')

def student_class(request):
	if request.method == 'POST':
		forms = StudentClassForm(request.POST)
		if forms.is_valid():
			forms.save()
			success = "Information Saved."
			context = {'msg':success, 'forms':forms}
			return redirect ('student-class')
		else:
			forms = StudentInfoForm()
			error = "Information didn't save."
			context = {'msg':error, 'forms':forms}
			return render(request,'academic/stdclass.html',context)
	forms = StudentClassForm()
	context = {'forms':forms}
	return render(request,'academic/stdclass.html',context)

def sub_form(request):
	if request.method == 'POST':
		forms = SubjectForm(request.POST)
		if forms.is_valid():
			forms.save()
			success = "Information Saved."
			context = {'msg':success, 'forms':forms}
			return redirect ('sub_form')
		else:
			forms = SubjectForm()
			error = "Information didn't save."
			context = {'msg':error, 'forms':forms}
			return render(request,'academic/std_subject.html',context)
	forms = SubjectForm()
	context = {'forms':forms}
	return render(request,'academic/std_subject.html',context)