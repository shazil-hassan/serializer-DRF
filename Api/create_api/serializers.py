from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=12)
    age=serializers.IntegerField()