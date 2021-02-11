from django.db import models


class Package(models.Model):

    name = models.CharField(max_length=100)
    min_value = models.DecimalField(max_digits=13, decimal_places=2)
    max_value = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    coefficient = models.DecimalField(max_digits=5, decimal_places=2)
