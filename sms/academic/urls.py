from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('student-class/',student_class,name='student-class'),
    path('subject-form/',sub_form,name='sub_form')
]