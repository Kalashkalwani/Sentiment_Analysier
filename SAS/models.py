from django.db import models

# Create your models here.

class History(models.Model):
    text = models.TextField()
    result = models.IntegerField(choices=[(0,0),(1,1)])
    Confidence = models.FloatField()

