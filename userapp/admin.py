from django.contrib import admin
from userapp.models import *


class UserRegistrationAdmin(admin.ModelAdmin):
    list_display    = ['user_name','user_email','mobile_number','user_type','user_pass','insert_date','status']
    search_fields   = ['user_name','user_email','mobile_number']
    list_filter     = ['user_type','status']

admin.site.register(UserRegistration, UserRegistrationAdmin)
