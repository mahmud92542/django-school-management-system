from django.shortcuts import render
#Jason Data return
from rest_framework.response import Response
#decorator import
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
#APIview er moddhe sob funtion ache
from rest_framework.views import APIView
#status import
from rest_framework.views import status
from .serializers import *
from academic.models import *

#decorator = view k access korar jonno permission
@api_view()
#API Creating
def check_user(request, user_name):

	isExist=User.objects.filter(username=user_name).exists()

	return Response({'status': isExist})

#class based API view
class StudentClassApi(APIView):
	def post(self,request):
		serializer = ClassSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'status':'OK'}, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#list API create
class ClassList(APIView):
	def get(self,request):
		clssList = StudentClass.objects.all()
		serializer = ClassSerializer(clssList, many=True)
		return Response(serializer.data)

#result API

class CheckResult(APIView):
	def post(self,request):
		serializer = CheckResultSerializer(data=request.data) #server k request dile, request.data er moddhe thake
		if serializer.is_valid():
			std_class = serializer.validated_data["std_class"]
			subject = serializer.validated_data["subject"]
			Student_id = serializer.validated_data["Student_id"]
			data = {'class':std_class, 'Student_id':Student_id }

			StudentResult.objects.filter(std_class__numeric_class=std_class,subject__name=subject,student__student_id=Student_id)

			return Response(data)
		return Response(serializer.errors)