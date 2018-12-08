from rest_framework import serializers
from academic.models import StudentClass
from result.models import *

class ClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentClass
		fields = '__all__'

#exclude = roll_number (roll number dekhabe na, exclude korle)

#result serializers
class CheckResultSerializer(serializers.Serializer):
	std_class = serializers.IntegerField()
	subject = serializers.CharField()
	Student_id = serializers.IntegerField()

class ResultSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentResults
		fields = '__all__'
