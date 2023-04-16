from django.db import models

# Create your models here.
class Plant(models.Model):
    SellerName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    # scientific_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,blank=True,default="")
    price = models.FloatField()
    image = models.CharField(max_length=1000,blank=True,default="")
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    number_people = models.IntegerField()
    bioScore = models.FloatField()
    image = models.CharField(max_length=1000)
    def __str__(self):
        return self.name