from django.contrib import admin
from .models import *

class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_name')
admin.site.register(StudentInfo,StudentInfoAdmin)
