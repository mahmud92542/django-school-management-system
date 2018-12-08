from django.db import models
from academic.models import *

class StudentInfo(models.Model):
	student_id = models.IntegerField(unique=True)
	student_name = models.CharField(max_length=40)
	GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
	student_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	student_photo = models.ImageField()
	student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
	student_section = models.CharField(max_length=1)

	def __str__(self):
		return self.student_name

