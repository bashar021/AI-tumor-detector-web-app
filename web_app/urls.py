from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # if the url is blank then calling the function of home page from the views file 
    path('', views.home,name="homepage"),
    path('pateint-image',views.pateint_image_data,name="imageForm"),
    path('pateint-data/',views.pateint_data,name="PateintData")
]
