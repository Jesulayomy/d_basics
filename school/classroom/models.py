from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    seat = models.IntegerField()
    is_representative = models.BooleanField(default=False)
    klass = models.ForeignKey(
        'Classroom',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='students',
    )

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    grade = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.grade
