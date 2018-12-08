from django.urls import path
from .views import *

urlpatterns = [
    path('check/user/<user_name>',check_user),
    path('add-class',StudentClassApi.as_view()), #as_view jate class k view hisebe dekhay
    path('class-list',ClassList.as_view()),
    path('check-result',CheckResult.as_view())
]