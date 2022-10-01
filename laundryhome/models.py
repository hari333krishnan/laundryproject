from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=250)
    house_name= models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    road_name = models.CharField(max_length=250)
    pincode = models.IntegerField()
    mobile = models.IntegerField()


    def __str__(self):
        return self.name


