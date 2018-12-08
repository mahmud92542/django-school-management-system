from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect

def std_result(request):
	if request.method == 'POST':
		forms = StudentResultsForm(request.POST)
		if forms.is_valid():
			forms.save()
			success = "Information Saved."
			context = {'msg':success, 'forms':forms}
			return redirect ('student-result')
		else:
			forms = StudentResultsForm()
			error = "Information didn't save."
			context = {'msg':error, 'forms':forms}
			return render(request,'StudentResultsForm.html',context)
	forms = StudentResultsForm()
	context = {'forms':forms}
	return render(request,'StudentResultsForm.html',context)