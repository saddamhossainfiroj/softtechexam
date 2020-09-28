from django.shortcuts import render, redirect
from . import models
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import random, string, os, smtplib, datetime, hashlib, json, xlsxwriter, pandas as pd
from django.http import JsonResponse, HttpResponse, Http404
from django.db.models import F, Q, Count, Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date 
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from PIL import Image
from django.utils.dateparse import parse_date
import os.path

def login(request):
    if request.method =="POST":
        user_email = request.POST["user_email"]          
        user_pass = request.POST["user_pass"].strip()
        hasher = PBKDF2PasswordHasher()
        user_pass = hasher.encode(password = request.POST["user_pass"], salt='salt', iterations=50000)
        chk_user = models.UserRegistration.objects.filter(user_email = user_email, user_pass = user_pass, status = True).first()
        if chk_user:
            request.session["user_id"] = chk_user.id
            request.session["user_img"] = str(chk_user.user_img)
            request.session["user_name"] = chk_user.user_name
            request.session["user_type"] = chk_user.user_type
            if chk_user.user_type == "admin":
                return redirect('/dashboard/')
            else:
                return redirect('/user-profile/')
        else:
            messages.warning(request, "User email or password is invalid!.")
            return render(request, 'settings/login.html')
    else:        
        return render(request, 'settings/login.html')

def base(request):  
    
    return render(request, 'settings/base.html')

def dashboard(request):  
    
    return render(request, 'settings/dashboard.html')

def user_registration(request):
    if request.method =="POST":
        user_name = request.POST["user_name"]  
        user_email = request.POST["user_email"]  
        mobile_number = request.POST["mobile_number"]          
        user_pass = request.POST["user_pass"].strip()
        hasher = PBKDF2PasswordHasher()
        user_pass = hasher.encode(password = request.POST["user_pass"], salt='salt', iterations=50000)
        user_image = ""
        if bool(request.FILES.get('user_image', False)) == True:
            user_image  = request.FILES['user_image']
            name, extension =os.path.splitext(str(user_image))
            if not os.path.exists('userapp/static/userapp/images/user_images/'):
                os.mkdir('userapp/static/userapp/images/user_images/')

            default_storage.save(settings.MEDIA_ROOT+"user_images/"+str(user_name)+str(extension), ContentFile(user_image.read()))
            user_image = "user_images/"+str(user_name)+str(extension)


        models.UserRegistration.objects.create(user_name = user_name, user_email = user_email, mobile_number = mobile_number, user_pass = user_pass, user_img = user_image, user_type = 'user')
        messages.success(request, "Registration Success.")
    
    return render(request, 'settings/user_registration.html')

def user_profile_update(request, id):
    if request.session["user_id"]:
        profile = models.UserRegistration.objects.filter(id = id, status = True).first()
        if request.method =="POST":
            user_name = request.POST["user_name"]  
            user_email = request.POST["user_email"]  
            mobile_number = request.POST["mobile_number"]        
            user_image = ""
            if bool(request.FILES.get('user_image', False)) == True:
                user_image  = request.FILES['user_image']
                name, extension =os.path.splitext(str(user_image))
                if not os.path.exists('userapp/static/userapp/images/user_images/'):
                    os.mkdir('userapp/static/userapp/images/user_images/')

                default_storage.save(settings.MEDIA_ROOT+"user_images/"+str(user_name)+str(extension), ContentFile(user_image.read()))
                user_image = "user_images/"+str(user_name)+str(extension)

            if user_image == "" and profile.user_img:
                user_image = profile.user_img
            models.UserRegistration.objects.filter(id = id).update(user_name = user_name, user_email = user_email, mobile_number = mobile_number, user_img = user_image)
            messages.success(request, "Registration Success.")
            if request.session["user_type"] == "admin":
                return redirect('/user-list/')
            else:
                return redirect('/user-profile/')
        else:
            return render(request, 'settings/user_profile_update.html', {'profile': profile,})
    else:
        return redirect('/')

def user_delete(request, id):
    if request.session["user_id"]:
        models.UserRegistration.objects.filter(id = id).delete()
        messages.success(request, "Delete Success.")
        if request.session["user_type"] == "admin":
            return redirect('/user-list/')
        else:
            return redirect('/')
        
    else:
        return redirect('/')

def signout(request):  
    try:
        return redirect("/")
    except:
        return redirect("/")

def user_profile(request):
    if request.session["user_id"]:
        profile = models.UserRegistration.objects.filter(id = int(request.session["user_id"]), status = True).first()

        return render(request, 'settings/user_profile.html',{'profile': profile,})
    else:
        return redirect('/')

def user_list(request):
    if request.session["user_id"]:
        user_list = models.UserRegistration.objects.all()

        return render(request, 'settings/user_list.html',{'user_list': user_list,})
    else:
        return redirect('/')