from django import forms
from .models import *

class StudentClassForm(forms.ModelForm):
	class Meta:
		model = StudentClass
		fields = ('name','numeric_class')
		widgets = {

		'name' : forms.TextInput(attrs={'class':'form-control'}),
		'numeric_class' : forms.NumberInput(attrs={'class':'form-control'})
		}

class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = '__all__'