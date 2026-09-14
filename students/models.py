from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=35)

    def __str__(self):
        return self.name


