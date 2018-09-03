from django.db import models

class Customer(models.Model):
    Customer_ID = models.IntegerField(primary_key = True)
    Customer_Name = models.CharField(max_length=25)
    Customer_Phone = models.CharField(max_length=30)
    Customer_Address = models.CharField(max_length=35)
    Customer_Occupation = models.CharField(max_length=20)
    Customer_Birthday = models.DateField()
    Customer_Gender = models.CharField(max_length=1)
