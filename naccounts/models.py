from django.db import models
from datetime import datetime
# Create your models here.
class Prediction(models.Model):
    
    patient_id=models.IntegerField()
    report=models.TextField(max_length=500)
    predictions=models.CharField(max_length=200, default='Negative')
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.patient_id)