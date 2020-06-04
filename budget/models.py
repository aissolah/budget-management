from django.db import models

# Create your models here.

class Budget(models.Model):
  name = models.CharField(max_length=250)
  month = models.IntegerField(blank=True)
  year = models.IntegerField(blank=True)
  is_archived = models.BooleanField()
  initial_amount = models.DecimalField(max_digits=8, decimal_places=2)
  total_amount = models.DecimalField(max_digits=8, decimal_places=2)


class Charge(models.Model):
  name = models.CharField(max_length=250)
  description = models.TextField(max_length=600, blank=True)
  amount = models.DecimalField(max_digits=8, decimal_places=2)
  is_archived = models.BooleanField()
  budget = models.ForeignKey('Budget', models.CASCADE)