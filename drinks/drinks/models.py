from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.quantity})'
