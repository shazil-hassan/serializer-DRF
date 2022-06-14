from rest_framework import serializers
from.models import Student
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=12)
    age=serializers.IntegerField()

    def create(self,validate_data):
        return Student.objects.create(**validate_data)    