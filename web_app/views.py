from django.shortcuts import render,HttpResponse,redirect
from web_app.forms import ImageForm
from web_app.models import upload_img
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode

# from django.shortcuts import render, redirect
# from django.urls import reverse
# import 
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_object  = form.instance
            Id = img_object.patient_image.name
            # print('it si actural name of the image')
            # print(Id)
            #  Id = img_object.patient_image.url
            base_url = '/pateint-data'  
            query_string =  urlencode({'image-id':Id})  
            url = '{}?{}'.format(base_url, query_string)  
            return redirect(url) 
        else:
            HttpResponse('please submit the form again ')
    
    return render(request,"Homepage.html")


def pateint_image_data(request):
    # to use media type  we have to setup some changes in the project 
    # make a forms.py file in your app dir 
    # if request.method == 'POST':
        # form = ImageForm(request.POST, request.FILES)
        # if form.is_valid():
        #     print("form has valid ")
            # form.save()
            # img_object  = form.instance

        
        # return HttpResponse("pateint data has been get ")
        # return render(request,"Diagnosis.html",{'form': form, 'img_obj': img_object})
        return redirect(reverse('pateint_data'))
    # return redirect("http://127.0.0.1:8000/pateint-data",{"foo":"bar"})
    # return redirect("/pateint-data",{"foo":"bar"})

    # return render(request,"Diagnosis.html",{'form': form, 'img_obj': img_object})
        # return redirect('/',form = form, img_obj = img_object)
        # return HttpResponseRedirect(reverse('/', img_obj=img_object))

    
def pateint_data(request):
    Image_id = request.GET.get('image-id') 
    # Image_id = Image_id.split("/")
    # new_Image_id = Image_id[1]
    # print(images.patient_image.name)
    images = upload_img.objects.filter( patient_image = Image_id).first()
    print(images.patient_image.url)
    # images = upload_img.objects.objects.filter(name = new_Image_id)
    # print(images.url)
    return render(request,'Diagnosis.html',{'img_url':images.patient_image.url})
# {'form': form, 'img_obj': img_object}
    # return HttpResponse('yes working ')
