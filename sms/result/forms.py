from django import forms
from .models import *

class StudentResultsForm(forms.ModelForm):
	class Meta:
		model = StudentResults
		fields = '__all__'
