from django.db import models

# Create your models here.
# Username
# Email
# Password => ConfrirmPassword (Password)

class Register(models.Model):
    Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
    
class Login(models.Model):
    Username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Username
    
    