from django.db import models

# Create your models here.

class History(models.Model):
    text = models.TextField()
    result = models.IntegerField()
    Confidence = models.FloatField()

