from django.db import models
from django.contrib.auth.models import User #(admin,admin12345)
from datetime import datetime

class SchoolInfo(models.Model):
	school_name = models.CharField(max_length = 150)
	phone = models.CharField(max_length = 15, unique = True)
	address = models.TextField(blank=True, null=True)
	photo = models.ImageField()
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.school_name

class StudentFees(models.Model):
	student_id = models.IntegerField()
	student_class = models.CharField(max_length=15)
	student_section = models.CharField(max_length=2)
	payment_type = models.IntegerField()
	month = models.CharField(max_length=15)
	date = models.DateTimeField(default=datetime.now())

class Payment(models.Model):
	student_id = models.IntegerField()
	student_name = models.CharField(max_length=30)

