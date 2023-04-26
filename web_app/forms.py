from django import forms 
# from .models import Image
from web_app.models import upload_img
from django.db import models  
from django.forms import fields 
from django.forms import ModelForm

class ImageForm(ModelForm):
    class Meta:
         # To specify the model to be used to create form  
        model = upload_img
         # It includes all the fields of model  
        fields = '__all__'
        # fields = ['name', 'upload image']
        # labels = {'phot':''}