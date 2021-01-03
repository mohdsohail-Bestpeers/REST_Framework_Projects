from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    code = models.IntegerField()

    def __str__(self):
        return self.course_name

class Student(models.Model):
    student_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students")
