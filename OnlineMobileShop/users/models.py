from django.db import models

# Create your models here.
class Order(models.Model):
    mobile=models.CharField(max_length=120)
    user=models.CharField(max_length=100)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=200)
    choices=(
        ("ordered","ordered"),("cancelled","cancelled"),("dispatched","dispatched")
    )
    status=models.CharField(max_length=100,choices=choices,default="ordered")


    def __str__(self):
        return self.mobile