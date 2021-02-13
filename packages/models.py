from django.db import models

from users.models import User


class Package(models.Model):

    name = models.CharField(max_length=100)
    min_value = models.DecimalField(max_digits=13, decimal_places=2)
    max_value = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    coefficient = models.DecimalField(max_digits=6, decimal_places=5)

    def __str__(self):
        return self.name


class Journal(models.Model):

    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal')
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, related_name='journal')
    old_balance = models.DecimalField(max_digits=13, decimal_places=2)
    coefficient = models.DecimalField(max_digits=6, decimal_places=5)
    new_balance = models.DecimalField(max_digits=13, decimal_places=2)

    class Meta:
        ordering = ['-date', '-id']
