from django import forms
from .models import *


class StudentInfoForm(forms.ModelForm):
	class Meta:
		model = StudentInfo
		fields = '__all__'