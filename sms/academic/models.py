from django.db import models

class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.username

class StudentClass(models.Model):
	name = models.CharField(max_length=50, unique=True)
	numeric_class = models.IntegerField(unique=True)
	

	def __str__(self):
		return self.name


class Subject(models.Model):
	subject_id = models.IntegerField(unique=True)
	subject_name = models.CharField(max_length=40)
	subject_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)

	def __str__(self):
		return self.subject_name

class Group(models.Model):
	group_id = models.IntegerField(unique=True)
	group_name = models.CharField(max_length=10)
	group_user = models.CharField(max_length=50)

	def __str__(self):
		return self.group_name



