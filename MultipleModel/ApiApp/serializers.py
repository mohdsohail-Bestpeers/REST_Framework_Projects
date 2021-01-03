from .models import Student, Course
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_name', 'city']

class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    class Meta:
        model = Course
        fields = ['course_name', 'code', 'students'] 

    def create(self, validated_data):
        students_data = validated_data.pop('students')
        obj = Course.objects.create(**validated_data)
        for student in students_data:
            Student.objects.create(course=obj, **student)
        return obj


    # def update(self, instance, validated_data):
    #     students_data = validated_data.pop('students')
    #     obj = (instance.students).all()
    #     obj = list(obj)
    #     instance.cource_name = validated_data.get('cource_name', instance.cource_name)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.students = validated_data.get('students', instance.students)
    #     instance.save()

    #     for student in students_data:
    #         obj1 = obj.pop(0)
    #         obj1.student_name = student.get('student_name', obj1.student_name)
    #         obj1.city = student.get('city', obj1.city)
    #         #obj1.num_stars = student.get('num_stars', obj1.num_stars)
    #         obj1.save()
    #     return instance