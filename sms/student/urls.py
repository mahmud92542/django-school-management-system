from django.urls import path
from .views import *

urlpatterns = [
    path('student-info/',studentinfo,name='student-info'),
]
