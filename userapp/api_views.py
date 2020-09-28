from django.shortcuts import render, redirect
from . import models
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import random, string, os, smtplib, datetime, hashlib, json, xlsxwriter, pandas as pd
from django.http import HttpResponse, JsonResponse, Http404
from django.core.serializers.json import DjangoJSONEncoder # This is use for encode json with date field, ex student date of birth
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

@csrf_exempt
def login(request):
    if request.method =="POST":
        user_email = request.POST["user_email"]          
        user_pass = request.POST["user_pass"].strip()
        hasher = PBKDF2PasswordHasher()
        user_pass = hasher.encode(password = request.POST["user_pass"], salt='salt', iterations=50000)
        chk_user = models.UserRegistration.objects.filter(user_email = user_email, user_pass = user_pass, status = True).first()
        
        if chk_user:
            data = {
                'status': True,
                'msg': "Login Success.",
                'user_id': str(chk_user.id)
            }
        else:
            data = {
                'status': False,
                'msg': "User ID or Password is invalid!."
            }
    
        return JsonResponse(data,  safe=False, content_type='application/json; charset=utf8')

@csrf_exempt
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


        regis = models.UserRegistration.objects.create(user_name = user_name, user_email = user_email, mobile_number = mobile_number, user_pass = user_pass, user_img = user_image, user_type = 'user')
        if regis:
            data = {
                'status': True,
                'msg': "Registration Success.",
                'user_id': str(regis.id)
            }
        else:
            data = {
                'status': False,
                'msg': "Registration Failed."
            }
    
        return JsonResponse(data,  safe=False, content_type='application/json; charset=utf8')

@csrf_exempt
def user_profile_update(request):
    if request.method =="POST":        
        id = int(request.POST["id"])
        user_name = request.POST["user_name"]  
        user_email = request.POST["user_email"]  
        mobile_number = request.POST["mobile_number"]    
        profile = models.UserRegistration.objects.filter(id = id, status = True).first()   
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
        regis = models.UserRegistration.objects.filter(id = id).update(user_name = user_name, user_email = user_email, mobile_number = mobile_number, user_img = user_image)
        if regis:
            data = {
                'status': True,
                'msg': "Update Success.",
            }
        else:
            data = {
                'status': False,
                'msg': "Update Failed."
            }
    
        return JsonResponse(data,  safe=False, content_type='application/json; charset=utf8')

@csrf_exempt
def user_delete(request):
    if request.method =="POST":
        id = int(request.POST["id"])
        delete = models.UserRegistration.objects.filter(id = id).delete()
        if delete:
            data = {
                'status': True,
                'msg': "Delete Success.",
            }
        else:
            data = {
                'status': False,
                'msg': "Delete Failed."
            }
    
        return JsonResponse(data,  safe=False, content_type='application/json; charset=utf8')

def user_list(request):
    user_list = list(models.UserRegistration.objects.values().all())

    if user_list:
        data = {
            'status': True,
            'msg': "Request Success.",
            'profile': user_list,
        }
    else:
        data = {
            'status': False,
            'msg': "Request Failed."
        }

    return JsonResponse(data,  safe=False, content_type='application/json; charset=utf8')