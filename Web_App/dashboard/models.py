from django.db import models

# Create your models here.
# Username
# Email
# Password => ConfrirmPassword (Password)

class Register(models.Model):
    Name = models.CharField()
    Username = models.CharField()
    Email = models.EmailField()
    Password = models.CharField()
    
    def __str__(self):
        return self.Name
    
class Login(models.Model):
    Username = models.CharField()
    Password = models.CharField()
    
    def __str__(self):
        return self.Username
    
    