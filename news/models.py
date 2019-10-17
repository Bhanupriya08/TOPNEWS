from django.db import models

# Create your models here.
class Adduser(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100,unique=True)
    #Username = models.CharField(max_length=100)
    #Password = models.CharField(max_length=40)
    Active = models.BooleanField(blank=True,default=False)


    def __str__(self):
        return "{}".format(self.Email)