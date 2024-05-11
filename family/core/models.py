from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=7, blank=True)
    family = models.ForeignKey(
        'Family',
        related_name='fam',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


class Family(models.Model):
    name = models.CharField(max_length=20)
    father = models.ForeignKey(
        'Person',
        on_delete=models.SET_NULL,
        related_name='family_father',
        null=True
    )
    children = models.ManyToManyField(
        Person,
        related_name='family_tree',
        blank=True,
    )
