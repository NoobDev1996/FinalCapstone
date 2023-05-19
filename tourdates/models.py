from django.db import models

# Create your models here.
class Tourdate(models.Model):
    date=models.DateField()
    location = models.CharField(max_length=100)