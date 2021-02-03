from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.brand_name


class Mobile(models.Model):
    mobile_name=models.CharField(max_length=100,unique=True)
    Mobile_brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    ram=models.CharField(max_length=100)
    internal_storage=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    screen_size=models.CharField(max_length=100)
    processor=models.CharField(max_length=100)
    price=models.IntegerField(default=1500)
    image=models.ImageField(upload_to="images")


    def __str__(self):
        return self.mobile_name
