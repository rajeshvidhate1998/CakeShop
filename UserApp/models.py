from django.db import models
from AdminApp.models import Cake

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)

    class Meta:
        db_table = "UserInfo"
        

class MyCart(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake,on_delete = models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = "MyCart"


class MyAccount(models.Model):
    cardno = models.CharField(max_length=16)
    cvv =  models.CharField(max_length=4)
    expiry = models.CharField(max_length=10)
    balance = models.FloatField(default=10000)

    class Meta:
        db_table = "MyAccount"





class OrderMaster(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    amount = models.FloatField(default=1000)
    dateOfOrder = models.DateField()

    class Meta:
        db_table = "OrderMaster"

