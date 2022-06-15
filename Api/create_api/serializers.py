from rest_framework import serializers
from.models import Student
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=12)
    age=serializers.IntegerField()

    def create(self,validate_data):
        return Student.objects.create(**validate_data)    

    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.phone=validated_data.get('phone',instance.phone)
        instance.age=validated_data.get('age',instance.age)

        instance.save()
        return instance
            