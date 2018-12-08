from django.db import models
from academic.models import *
from student.models import *

class StudentResults(models.Model):
	std_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
	section = models.CharField(max_length=2)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	total_marks = models.IntegerField(default=100)
	obtain_marks = models.DecimalField(max_digits=5, decimal_places=2)
	student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)

	def __str__(self):
		return self.student.student_name
