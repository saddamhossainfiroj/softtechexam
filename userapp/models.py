from django.db import models

class UserRegistration(models.Model):
    user_name   =  models.CharField(max_length=100)  
    user_email  = models.EmailField(max_length=100) 
    mobile_number = models.CharField(max_length=15) 
    user_pass   = models.CharField(max_length = 200)
    user_img    = models.ImageField(upload_to='user_images') 
    insert_date = models.DateTimeField(auto_now_add=True)
    user_types = (
        ('user', 'user'),
        ('admin', 'admin'),
    )
    user_type   = models.CharField(max_length=20, choices=user_types)
    last_update = models.DateTimeField(auto_now=True)
    insert_by   = models.IntegerField(default=0)
    update_by   = models.IntegerField(default=0)   
    status      = models.BooleanField(default=True) 
    
    def __str__(self):
        return str(self.user_name)   
        
    class Meta:
        verbose_name = "User Registration"
        verbose_name_plural = "User Registration"  