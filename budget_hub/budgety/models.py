from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    address1 = models.CharField(max_length=100)
    Bank_name = models.CharField(max_length=100)
    Branch = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    # account_name = models.CharField(max_length=50)
    card_number = models.FloatField(default=50)
    bvn = models.FloatField(default=50)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    phone_number = models.CharField(max_length=15,blank=True)
    amount = models.FloatField(default=0.0,blank=True)

class Budget(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    is_income = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)