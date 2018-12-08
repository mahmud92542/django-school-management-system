from django.shortcuts import render
from .models import *
from .forms import *


def studentinfo(request):
	if request.method == 'POST':
		forms = StudentInfoForm(request.POST, request.FILES)#for image file request.FIELS
		if forms.is_valid():
			forms.save()
			success = "Information Saved."
			context = {'msg':success, 'forms':forms}
			return render (request,'studentinfo.html',context)
		else:
			forms = StudentInfoForm()
			error = "Information didn't save."
			context = {'msg':error, 'forms':forms}
			return render(request,'studentinfo.html',context)
	forms = StudentInfoForm()
	context = {'forms':forms}
	return render (request,'studentinfo.html',context)