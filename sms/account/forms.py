from django import forms
from django.core.exceptions import ValidationError
from .models import *

def password_checker(value):
	if len(value) < 8:
		raise ValidationError('Password must be more than 8 character.')


class UserRegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),validators=[password_checker])
	re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	#password match
	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get('password')
		re_password = cleaned_data.get('re_password')

		if password != re_password:
			raise forms.ValidationError("Password doesn't match.")

#Login form

class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SchoolInfoForm(forms.ModelForm):
	class Meta:
		model = SchoolInfo
		fields = '__all__'

class StudentFeesForm(forms.ModelForm):
	class Meta:
			model = StudentFees
			fields = '__all__'