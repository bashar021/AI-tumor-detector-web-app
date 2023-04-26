from django.db import models
from django import forms
 

# Create your models here.

class upload_img(models.Model):
    name = forms.CharField()
    patient_image = models.ImageField(upload_to='images')
    # def __str__(self):
    #     return self.caption
