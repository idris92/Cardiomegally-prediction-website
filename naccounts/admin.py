from django.contrib import admin
from .models import Prediction
# Register your models here.
class MpredictionAdmin(admin.ModelAdmin):
    list_display=('patient_id','predictions')
admin.site.register(Prediction)