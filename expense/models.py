from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.TextField()
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name 