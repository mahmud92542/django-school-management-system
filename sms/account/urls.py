from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='user_register'),
    path('login/',user_login, name='user_login'),
    path('logout',user_logout, name='user_logout' ),
    path('school-info/',SchoolInfo,name='school-info'),
    path('student-fees/',StudentFees,name='student-fees')
]
