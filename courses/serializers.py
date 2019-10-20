from rest_framework import serializers
from .models import Course
#This is our serializer page
class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Course
		fields = ('id','url','name','language','price')
		